# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import hashlib
from ccxt.base.errors import ExchangeError


class crypton (Exchange):

    def describe(self):
        return self.deep_extend(super(crypton, self).describe(), {
            'id': 'crypton',
            'name': 'Crypton',
            'countries': ['EU'],
            'rateLimit': 500,
            'version': '1',
            'has': {
                'fetchDepositAddress': True,
                'fetchMyTrades': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchTicker': False,
                'fetchTickers': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/41334251-905b5a78-6eed-11e8-91b9-f3aa435078a1.jpg',
                'api': 'https://api.cryptonbtc.com',
                'www': 'https://cryptonbtc.com',
                'doc': 'https://cryptonbtc.docs.apiary.io/',
                'fees': 'https://help.cryptonbtc.com/hc/en-us/articles/360004089872-Fees',
            },
            'api': {
                'public': {
                    'get': [
                        'currencies',
                        'markets',
                        'markets/{id}',
                        'markets/{id}/orderbook',
                        'markets/{id}/trades',
                        'tickers',
                    ],
                },
                'private': {
                    'get': [
                        'balances',
                        'orders',
                        'orders/{id}',
                        'fills',
                        'deposit_address/{currency}',
                        'deposits',
                    ],
                    'post': [
                        'orders',
                    ],
                    'delete': [
                        'orders/{id}',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'maker': 0.0020,
                    'taker': 0.0020,
                },
            },
        })

    def fetch_markets(self, params={}):
        response = self.publicGetMarkets(params)
        markets = response['result']
        result = []
        keys = list(markets.keys())
        for i in range(0, len(keys)):
            id = keys[i]
            market = markets[id]
            baseId = self.safe_string(market, 'base')
            quoteId = self.safe_string(market, 'quote')
            base = self.common_currency_code(baseId)
            quote = self.common_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'amount': 8,
                'price': self.precision_from_string(self.safe_string(market, 'priceStep')),
            }
            active = market['enabled']
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': active,
                'info': market,
                'precision': precision,
                'limits': {
                    'amount': {
                        'min': self.safe_float(market, 'minSize'),
                        'max': None,
                    },
                    'price': {
                        'min': self.safe_float(market, 'priceStep'),
                        'max': None,
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                },
            })
        return result

    def fetch_balance(self, params={}):
        self.load_markets()
        balances = self.privateGetBalances(params)
        result = {'info': balances}
        keys = list(balances.keys())
        for i in range(0, len(keys)):
            id = keys[i]
            currency = self.common_currency_code(id)
            account = self.account()
            balance = balances[id]
            account['total'] = self.safe_float(balance, 'total')
            account['free'] = self.safe_float(balance, 'free')
            account['used'] = self.safe_float(balance, 'locked')
            result[currency] = account
        return self.parse_balance(result)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        request = {
            'id': self.market_id(symbol),
        }
        response = self.publicGetMarketsIdOrderbook(self.extend(request, params))
        return self.parse_order_book(response)

    def parse_ticker(self, ticker, market=None):
        symbol = None
        if market is not None:
            symbol = market['symbol']
        last = self.safe_float(ticker, 'last')
        relativeChange = self.safe_float(ticker, 'change24h', 0.0)
        return {
            'symbol': symbol,
            'timestamp': None,
            'datetime': None,
            'high': None,
            'low': None,
            'bid': self.safe_float(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'ask'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': relativeChange * 100,
            'average': None,
            'baseVolume': self.safe_float(ticker, 'volume24h'),
            'quoteVolume': None,
            'info': ticker,
        }

    def fetch_tickers(self, symbols=None, params={}):
        self.load_markets()
        response = self.publicGetTickers(params)
        tickers = self.safe_value(response, 'result')
        keys = list(tickers.keys())
        result = {}
        for i in range(0, len(keys)):
            id = keys[i]
            ticker = tickers[id]
            market = None
            symbol = id
            if id in self.markets_by_id:
                market = self.markets_by_id[id]
                symbol = market['symbol']
            else:
                symbol = self.parse_symbol(id)
            result[symbol] = self.parse_ticker(ticker, market)
        return result

    def parse_trade(self, trade, market=None):
        timestamp = self.parse8601(self.safe_string(trade, 'time'))
        symbol = None
        marketId = self.safe_string(trade, 'market')
        if marketId in self.markets_by_id:
            market = self.markets_by_id[marketId]
        if symbol is None:
            if market is not None:
                symbol = market['symbol']
        feeCost = self.safe_float(trade, 'fee')
        fee = None
        if feeCost is not None:
            feeCurrencyId = self.safe_string(trade, 'feeCurrency')
            feeCurrencyCode = self.common_currency_code(feeCurrencyId)
            fee = {
                'cost': feeCost,
                'currency': feeCurrencyCode,
            }
        id = self.safe_string(trade, 'id')
        side = self.safe_string(trade, 'side')
        orderId = self.safe_string(trade, 'orderId')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'size')
        cost = None
        if price is not None:
            if amount is not None:
                cost = amount * price
        return {
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': None,
            'side': side,
            'order': orderId,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'id': market['id'],
        }
        if limit is not None:
            request['limit'] = limit
        response = self.publicGetMarketsIdTrades(self.extend(request, params))
        #
        #     {
        #         "result":[
        #             {
        #                 "id":4256381,
        #                 "price":7901.56,
        #                 "side":"buy",
        #                 "size":0.75708114,
        #                 "time":"2019-05-14T16:15:46.781653+00:00"
        #             }
        #         ],
        #         "success":true
        #     }
        #
        return self.parse_trades(response['result'], market, since, limit)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {}
        if limit is not None:
            request['limit'] = limit
        response = self.privateGetFills(self.extend(request, params))
        trades = self.parse_trades(response['result'], market, since, limit)
        return self.filter_by_symbol(trades, symbol)

    def parse_order(self, order, market=None):
        id = self.safe_string(order, 'id')
        status = self.safe_string(order, 'status')
        side = self.safe_string(order, 'side')
        type = self.safe_string(order, 'type')
        symbol = None
        marketId = self.safe_string(order, 'market')
        if marketId in self.markets_by_id:
            market = self.markets_by_id[marketId]
            symbol = market['symbol']
        else:
            symbol = self.parse_symbol(marketId)
        timestamp = self.parse8601(self.safe_string(order, 'createdAt'))
        feeCost = self.safe_float(order, 'fee')
        fee = None
        if feeCost is not None:
            feeCurrencyId = self.safe_string(order, 'feeCurrency')
            feeCurrencyCode = self.common_currency_code(feeCurrencyId)
            fee = {
                'cost': feeCost,
                'currency': feeCurrencyCode,
            }
        price = self.safe_float(order, 'price')
        amount = self.safe_float(order, 'size')
        filled = self.safe_float(order, 'filledSize')
        remaining = amount - filled
        cost = filled * price
        return {
            'info': order,
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'cost': cost,
            'average': None,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': fee,
        }

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'id': id,
        }
        response = self.privateGetOrdersId(self.extend(request, params))
        return self.parse_order(response['result'])

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            request['market'] = self.market_id(symbol)
        response = self.privateGetOrders(self.extend(request, params))
        return self.parse_orders(response['result'], market, since, limit)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        request = {
            'market': self.market_id(symbol),
            'side': side,
            'type': type,
            'size': self.amount_to_precision(symbol, amount),
            'price': self.price_to_precision(symbol, price),
        }
        response = self.privatePostOrders(self.extend(request, params))
        return self.parse_order(response['result'])

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'id': id,
        }
        response = self.privateDeleteOrdersId(self.extend(request, params))
        return self.parse_order(response['result'])

    def parse_symbol(self, id):
        base, quote = id.split('-')
        base = self.common_currency_code(base)
        quote = self.common_currency_code(quote)
        return base + '/' + quote

    def fetch_deposit_address(self, code, params={}):
        self.load_markets()
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
        }
        response = self.privateGetDepositAddressCurrency(self.extend(request, params))
        result = self.safe_value(response, 'result')
        address = self.safe_string(result, 'address')
        tag = self.safe_string(result, 'tag')
        self.check_address(address)
        return {
            'currency': code,
            'address': address,
            'tag': tag,
            'info': response,
        }

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        request = '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        if method == 'GET':
            if query:
                request += '?' + self.urlencode(query)
        url = self.urls['api'] + request
        if api == 'private':
            self.check_required_credentials()
            timestamp = str(self.milliseconds())
            payload = ''
            if method != 'GET':
                if query:
                    body = self.json(query)
                    payload = body
            auth = timestamp + method + request + payload
            signature = self.hmac(self.encode(auth), self.encode(self.secret), hashlib.sha256)
            headers = {
                'CRYPTON-APIKEY': self.apiKey,
                'CRYPTON-SIGNATURE': signature,
                'CRYPTON-TIMESTAMP': timestamp,
                'Content-Type': 'application/json',
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return
        success = self.safe_value(response, 'success')
        if not success:
            raise ExchangeError(self.id + ' ' + body)
