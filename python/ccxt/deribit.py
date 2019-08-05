# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import NotSupported
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import ExchangeNotAvailable


class deribit(Exchange):

    def describe(self):
        return self.deep_extend(super(deribit, self).describe(), {
            'id': 'deribit',
            'name': 'Deribit',
            'countries': ['NL'],  # Netherlands
            'version': 'v1',
            'userAgent': None,
            'rateLimit': 2000,
            'has': {
                'CORS': True,
                'editOrder': True,
                'fetchOrder': True,
                'fetchOrders': False,
                'fetchOpenOrders': True,
                'fetchClosedOrders': True,
                'fetchMyTrades': True,
                'fetchTickers': False,
            },
            'urls': {
                'test': 'https://test.deribit.com',
                'logo': 'https://user-images.githubusercontent.com/1294454/41933112-9e2dd65a-798b-11e8-8440-5bab2959fcb8.jpg',
                'api': 'https://www.deribit.com',
                'www': 'https://www.deribit.com',
                'doc': [
                    'https://docs.deribit.com',
                    'https://github.com/deribit',
                ],
                'fees': 'https://www.deribit.com/pages/information/fees',
                'referral': 'https://www.deribit.com/reg-1189.4038',
            },
            'api': {
                'public': {
                    'get': [
                        'ping',
                        'test',
                        'getinstruments',
                        'index',
                        'getcurrencies',
                        'getorderbook',
                        'getlasttrades',
                        'getsummary',
                        'stats',
                        'getannouncments',
                    ],
                },
                'private': {
                    'get': [
                        'account',
                        'getopenorders',
                        'positions',
                        'orderhistory',
                        'orderstate',
                        'tradehistory',
                        'newannouncements',
                    ],
                    'post': [
                        'buy',
                        'sell',
                        'edit',
                        'cancel',
                        'cancelall',
                    ],
                },
            },
            'exceptions': {
                # 0 or absent Success, No error
                '9999': PermissionDenied,   # "api_not_enabled" User didn't enable API for the Account
                '10000': AuthenticationError,  # "authorization_required" Authorization issue, invalid or absent signature etc
                '10001': ExchangeError,     # "error" Some general failure, no public information available
                '10002': InvalidOrder,      # "qty_too_low" Order quantity is too low
                '10003': InvalidOrder,      # "order_overlap" Rejection, order overlap is found and self-trading is not enabled
                '10004': OrderNotFound,     # "order_not_found" Attempt to operate with order that can't be found by specified id
                '10005': InvalidOrder,      # "price_too_low <Limit>" Price is too low, <Limit> defines current limit for the operation
                '10006': InvalidOrder,      # "price_too_low4idx <Limit>" Price is too low for current index, <Limit> defines current bottom limit for the operation
                '10007': InvalidOrder,  # "price_too_high <Limit>" Price is too high, <Limit> defines current up limit for the operation
                '10008': InvalidOrder,  # "price_too_high4idx <Limit>" Price is too high for current index, <Limit> defines current up limit for the operation
                '10009': InsufficientFunds,  # "not_enough_funds" Account has not enough funds for the operation
                '10010': OrderNotFound,  # "already_closed" Attempt of doing something with closed order
                '10011': InvalidOrder,  # "price_not_allowed" This price is not allowed for some reason
                '10012': InvalidOrder,  # "book_closed" Operation for instrument which order book had been closed
                '10013': PermissionDenied,  # "pme_max_total_open_orders <Limit>" Total limit of open orders has been exceeded, it is applicable for PME users
                '10014': PermissionDenied,  # "pme_max_future_open_orders <Limit>" Limit of count of futures' open orders has been exceeded, it is applicable for PME users
                '10015': PermissionDenied,  # "pme_max_option_open_orders <Limit>" Limit of count of options' open orders has been exceeded, it is applicable for PME users
                '10016': PermissionDenied,  # "pme_max_future_open_orders_size <Limit>" Limit of size for futures has been exceeded, it is applicable for PME users
                '10017': PermissionDenied,  # "pme_max_option_open_orders_size <Limit>" Limit of size for options has been exceeded, it is applicable for PME users
                '10019': PermissionDenied,  # "locked_by_admin" Trading is temporary locked by admin
                '10020': ExchangeError,  # "invalid_or_unsupported_instrument" Instrument name is not valid
                '10022': InvalidOrder,  # "invalid_quantity" quantity was not recognized as a valid number
                '10023': InvalidOrder,  # "invalid_price" price was not recognized as a valid number
                '10024': InvalidOrder,  # "invalid_max_show" max_show parameter was not recognized as a valid number
                '10025': InvalidOrder,  # "invalid_order_id" Order id is missing or its format was not recognized as valid
                '10026': InvalidOrder,  # "price_precision_exceeded" Extra precision of the price is not supported
                '10027': InvalidOrder,  # "non_integer_contract_amount" Futures contract amount was not recognized as integer
                '10028': DDoSProtection,  # "too_many_requests" Allowed request rate has been exceeded
                '10029': OrderNotFound,  # "not_owner_of_order" Attempt to operate with not own order
                '10030': ExchangeError,  # "must_be_websocket_request" REST request where Websocket is expected
                '10031': ExchangeError,  # "invalid_args_for_instrument" Some of arguments are not recognized as valid
                '10032': InvalidOrder,  # "whole_cost_too_low" Total cost is too low
                '10033': NotSupported,  # "not_implemented" Method is not implemented yet
                '10034': InvalidOrder,  # "stop_price_too_high" Stop price is too high
                '10035': InvalidOrder,  # "stop_price_too_low" Stop price is too low
                '11035': InvalidOrder,  # "no_more_stops <Limit>" Allowed amount of stop orders has been exceeded
                '11036': InvalidOrder,  # "invalid_stoppx_for_index_or_last" Invalid StopPx(too high or too low) as to current index or market
                '11037': InvalidOrder,  # "outdated_instrument_for_IV_order" Instrument already not available for trading
                '11038': InvalidOrder,  # "no_adv_for_futures" Advanced orders are not available for futures
                '11039': InvalidOrder,  # "no_adv_postonly" Advanced post-only orders are not supported yet
                '11040': InvalidOrder,  # "impv_not_in_range 0..499%" Implied volatility is out of allowed range
                '11041': InvalidOrder,  # "not_adv_order" Advanced order properties can't be set if the order is not advanced
                '11042': PermissionDenied,  # "permission_denied" Permission for the operation has been denied
                '11044': OrderNotFound,  # "not_open_order" Attempt to do open order operations with the not open order
                '11045': ExchangeError,  # "invalid_event" Event name has not been recognized
                '11046': ExchangeError,  # "outdated_instrument" At several minutes to instrument expiration, corresponding advanced implied volatility orders are not allowed
                '11047': ExchangeError,  # "unsupported_arg_combination" The specified combination of arguments is not supported
                '11048': ExchangeError,  # "not_on_self_server" The requested operation is not available on self server.
                '11050': ExchangeError,  # "invalid_request" Request has not been parsed properly
                '11051': ExchangeNotAvailable,  # "system_maintenance" System is under maintenance
                '11030': ExchangeError,  # "other_reject <Reason>" Some rejects which are not considered as very often, more info may be specified in <Reason>
                '11031': ExchangeError,  # "other_error <Error>" Some errors which are not considered as very often, more info may be specified in <Error>
            },
            'options': {
                'fetchTickerQuotes': True,
            },
        })

    @staticmethod
    def get_symbol_to_unified_symbol_dict(markets):
        symbol_to_unified_symbol_dict = dict()
        for market in markets["result"]:
            _id, base, quote = market["instrumentName"], market['baseCurrency'], market['currency']
            tokens = _id.split("-")
            if len(tokens) > 2:
                continue
            identifier = tokens[-1]
            if identifier == "PERPETUAL":
                symbol = base + "/" + quote
            else:
                symbol = base + "/" + identifier
            symbol_to_unified_symbol_dict[symbol] = _id
        return {_id: symbol for symbol, _id in symbol_to_unified_symbol_dict.items()}

    def fetch_markets(self, params={}):
        response = self.publicGetGetinstruments(params)
        markets = self.safe_value(response, 'result')
        result = []
        symbol_to_unified_symbol_dict = self.get_symbol_to_unified_symbol_dict(response)
        for i in range(0, len(markets)):
            market = markets[i]
            id = self.safe_string(market, 'instrumentName')
            baseId = self.safe_string(market, 'baseCurrency')
            quoteId = self.safe_string(market, 'currency')
            base = self.common_currency_code(baseId)
            quote = self.common_currency_code(quoteId)
            symbol = symbol_to_unified_symbol_dict.get(id, id)
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'active': market['isActive'],
                'precision': {
                    'amount': market['minTradeSize'],
                    'price': market['tickSize'],
                },
                'limits': {
                    'amount': {
                        'min': market['minTradeSize'],
                    },
                    'price': {
                        'min': market['tickSize'],
                    },
                },
                'type': market['kind'],
                'spot': False,
                'future': market['kind'] == 'future',
                'option': market['kind'] == 'option',
                'info': market,
            })
        return result

    def fetch_balance(self, params={}):
        response = self.privateGetAccount(params)
        result = {
            'BTC': {
                'free': self.safe_float(response['result'], 'availableFunds'),
                'used': self.safe_float(response['result'], 'maintenanceMargin'),
                'total': self.safe_float(response['result'], 'equity'),
            },
        }
        return self.parse_balance(result)

    def fetch_deposit_address(self, currency, params={}):
        response = self.privateGetAccount(params)
        address = self.safe_string(response, 'depositAddress')
        return {
            'currency': self.common_currency_code('BTC'),
            'address': address,
            'tag': None,
            'info': response,
        }

    def parse_ticker(self, ticker, market=None):
        timestamp = self.safe_integer(ticker, 'created')
        symbol = self.find_symbol(self.safe_string(ticker, 'instrumentName'), market)
        last = self.safe_float(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'high'),
            'low': self.safe_float(ticker, 'low'),
            'bid': self.safe_float(ticker, 'bidPrice'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'askPrice'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': None,
            'quoteVolume': self.safe_float(ticker, 'volume'),
            'info': ticker,
        }

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument': market['id'],
        }
        response = self.publicGetGetsummary(self.extend(request, params))
        return self.parse_ticker(response['result'], market)

    def parse_trade(self, trade, market=None):
        #
        # fetchTrades(public)
        #
        #     {
        #         "tradeId":23197559,
        #         "instrument":"BTC-28JUN19",
        #         "timeStamp":1559643011379,
        #         "tradeSeq":1997200,
        #         "quantity":2,
        #         "amount":20.0,
        #         "price":8010.0,
        #         "direction":"sell",
        #         "tickDirection":2,
        #         "indexPrice":7969.01
        #     }
        #
        # fetchMyTrades(private)
        #
        #     {
        #         "quantity":54,
        #         "amount":540.0,
        #         "tradeId":23087297,
        #         "instrument":"BTC-PERPETUAL",
        #         "timeStamp":1559604178803,
        #         "tradeSeq":8265011,
        #         "price":8213.0,
        #         "side":"sell",
        #         "orderId":12373631800,
        #         "matchingId":0,
        #         "liquidity":"T",
        #         "fee":0.000049312,
        #         "feeCurrency":"BTC",
        #         "tickDirection":3,
        #         "indexPrice":8251.94,
        #         "selfTrade":false
        #     }
        #
        id = self.safe_string(trade, 'tradeId')
        orderId = self.safe_string(trade, 'orderId')
        symbol = None
        if market is not None:
            symbol = market['symbol']
        timestamp = self.safe_integer(trade, 'timeStamp')
        side = self.safe_string_2(trade, 'side', 'direction')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'quantity')
        cost = None
        if amount is not None:
            if price is not None:
                cost = amount * price
        fee = None
        feeCost = self.safe_float(trade, 'fee')
        if feeCost is not None:
            feeCurrencyId = self.safe_string(trade, 'feeCurrency')
            feeCurrencyCode = self.common_currency_code(feeCurrencyId)
            fee = {
                'cost': feeCost,
                'currency': feeCurrencyCode,
            }
        return {
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'order': orderId,
            'type': None,
            'side': side,
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
            'instrument': market['id'],
        }
        if limit is not None:
            request['limit'] = limit
        else:
            request['limit'] = 10000
        response = self.publicGetGetlasttrades(self.extend(request, params))
        #
        #     {
        #         "usOut":1559643108984527,
        #         "usIn":1559643108984470,
        #         "usDiff":57,
        #         "testnet":false,
        #         "success":true,
        #         "result": [
        #             {
        #                 "tradeId":23197559,
        #                 "instrument":"BTC-28JUN19",
        #                 "timeStamp":1559643011379,
        #                 "tradeSeq":1997200,
        #                 "quantity":2,
        #                 "amount":20.0,
        #                 "price":8010.0,
        #                 "direction":"sell",
        #                 "tickDirection":2,
        #                 "indexPrice":7969.01
        #             }
        #         ],
        #         "message":""
        #     }
        #
        result = self.safe_value(response, 'result', [])
        return self.parse_trades(result, market, since, limit)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument': market['id'],
        }
        response = self.publicGetGetorderbook(self.extend(request, params))
        timestamp = self.safe_integer(response, 'usOut') / 1000
        orderbook = self.parse_order_book(response['result'], timestamp, 'bids', 'asks', 'price', 'quantity')
        return self.extend(orderbook, {
            'nonce': self.safe_integer(response, 'tstamp'),
        })

    def parse_order_status(self, status):
        statuses = {
            'open': 'open',
            'cancelled': 'canceled',
            'filled': 'closed',
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        #
        #     {
        #         "orderId": 5258039,          # ID of the order
        #         "type": "limit",             # not documented, but present in the actual response
        #         "instrument": "BTC-26MAY17",  # instrument name(market id)
        #         "direction": "sell",         # order direction, "buy" or "sell"
        #         "price": 1860,               # float, USD for futures, BTC for options
        #         "label": "",                 # label set by the owner, up to 32 chars
        #         "quantity": 10,              # quantity, in contracts($10 per contract for futures, ฿1 — for options)
        #         "filledQuantity": 3,         # filled quantity, in contracts($10 per contract for futures, ฿1 — for options)
        #         "avgPrice": 1860,            # average fill price of the order
        #         "commission": -0.000001613,  # in BTC units
        #         "created": 1494491899308,    # creation timestamp
        #         "state": "open",             # open, cancelled, etc
        #         "postOnly": False            # True for post-only orders only
        # open orders --------------------------------------------------------
        #         "lastUpdate": 1494491988754,  # timestamp of the last order state change(before self cancelorder of course)
        # closed orders ------------------------------------------------------
        #         "tstamp": 1494492913288,     # timestamp of the last order state change, documented, but may be missing in the actual response
        #         "modified": 1494492913289,   # timestamp of the last db write operation, e.g. trade that doesn't change order status, documented, but may missing in the actual response
        #         "adv": False                 # advanced type(false, or "usd" or "implv")
        #         "trades": [],                # not documented, injected from the outside of the parseOrder method into the order
        #     }
        #
        timestamp = self.safe_integer(order, 'created')
        lastUpdate = self.safe_integer(order, 'lastUpdate')
        lastTradeTimestamp = self.safe_integer_2(order, 'tstamp', 'modified')
        id = self.safe_string(order, 'orderId')
        price = self.safe_float(order, 'price')
        average = self.safe_float(order, 'avgPrice')
        amount = self.safe_float(order, 'quantity')
        filled = self.safe_float(order, 'filledQuantity')
        if lastTradeTimestamp is None:
            if filled is not None:
                if filled > 0:
                    lastTradeTimestamp = lastUpdate
        remaining = None
        cost = None
        if filled is not None:
            if amount is not None:
                remaining = amount - filled
            if price is not None:
                cost = price * filled
        status = self.parse_order_status(self.safe_string(order, 'state'))
        side = self.safe_string(order, 'direction')
        if side is not None:
            side = side.lower()
        feeCost = self.safe_float(order, 'commission')
        if feeCost is not None:
            feeCost = abs(feeCost)
        fee = {
            'cost': feeCost,
            'currency': 'BTC',
        }
        type = self.safe_string(order, 'type')
        marketId = self.safe_string(order, 'instrument')
        symbol = None
        if marketId in self.markets_by_id:
            market = self.markets_by_id[marketId]
            symbol = market['symbol']
        return {
            'info': order,
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': lastTradeTimestamp,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'average': average,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': fee,
            'trades': None,  # todo: parse trades
        }

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'orderId': id,
        }
        response = self.privateGetOrderstate(self.extend(request, params))
        result = self.safe_value(response, 'result')
        if result is None:
            raise OrderNotFound(self.id + ' fetchOrder() ' + self.json(response))
        return self.parse_order(result)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        request = {
            'instrument': self.market_id(symbol),
            'quantity': amount,
            'type': type,
            # 'post_only': 'false' or 'true', https://github.com/ccxt/ccxt/issues/5159
        }
        if price is not None:
            request['price'] = price
        method = 'privatePost' + self.capitalize(side)
        response = getattr(self, method)(self.extend(request, params))
        order = self.safe_value(response['result'], 'order')
        if order is None:
            return response
        return self.parse_order(order)

    def edit_order(self, id, symbol, type, side, amount=None, price=None, params={}):
        self.load_markets()
        request = {
            'orderId': id,
        }
        if amount is not None:
            request['quantity'] = amount
        if price is not None:
            request['price'] = price
        response = self.privatePostEdit(self.extend(request, params))
        return self.parse_order(response['result']['order'])

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'orderId': id,
        }
        response = self.privatePostCancel(self.extend(request, params))
        return self.parse_order(response['result']['order'])

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchClosedOrders() requires a `symbol` argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument': market['id'],
        }
        response = self.privateGetGetopenorders(self.extend(request, params))
        return self.parse_orders(response['result'], market, since, limit)

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchClosedOrders() requires a `symbol` argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument': market['id'],
        }
        response = self.privateGetOrderhistory(self.extend(request, params))
        return self.parse_orders(response['result'], market, since, limit)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument': market['id'],
        }
        if limit is not None:
            request['count'] = limit  # default = 20
        response = self.privateGetTradehistory(self.extend(request, params))
        #
        #     {
        #         "usOut":1559611553394836,
        #         "usIn":1559611553394000,
        #         "usDiff":836,
        #         "testnet":false,
        #         "success":true,
        #         "result": [
        #             {
        #                 "quantity":54,
        #                 "amount":540.0,
        #                 "tradeId":23087297,
        #                 "instrument":"BTC-PERPETUAL",
        #                 "timeStamp":1559604178803,
        #                 "tradeSeq":8265011,
        #                 "price":8213.0,
        #                 "side":"sell",
        #                 "orderId":12373631800,
        #                 "matchingId":0,
        #                 "liquidity":"T",
        #                 "fee":0.000049312,
        #                 "feeCurrency":"BTC",
        #                 "tickDirection":3,
        #                 "indexPrice":8251.94,
        #                 "selfTrade":false
        #             }
        #         ],
        #         "message":"",
        #         "has_more":true
        #     }
        #
        trades = self.safe_value(response, 'result', [])
        return self.parse_trades(trades, market, since, limit)

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        query = '/' + 'api/' + self.version + '/' + api + '/' + path
        url = self.urls['api'] + query
        if api == 'public':
            if params:
                url += '?' + self.urlencode(params)
        else:
            self.check_required_credentials()
            nonce = str(self.nonce())
            auth = '_=' + nonce + '&_ackey=' + self.apiKey + '&_acsec=' + self.secret + '&_action=' + query
            if params:
                params = self.keysort(params)
                auth += '&' + self.urlencode(params)
            hash = self.hash(self.encode(auth), 'sha256', 'base64')
            signature = self.apiKey + '.' + nonce + '.' + self.decode(hash)
            headers = {
                'x-deribit-sig': signature,
            }
            if method != 'GET':
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
                body = self.urlencode(params)
            elif params:
                url += '?' + self.urlencode(params)
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, httpCode, reason, url, method, headers, body, response):
        if not response:
            return  # fallback to default error handler
        #
        #     {"usOut":1535877098645376,"usIn":1535877098643364,"usDiff":2012,"testnet":false,"success":false,"message":"order_not_found","error":10004}
        #
        error = self.safe_string(response, 'error')
        if (error is not None) and(error != '0'):
            feedback = self.id + ' ' + body
            exceptions = self.exceptions
            if error in exceptions:
                raise exceptions[error](feedback)
            raise ExchangeError(feedback)  # unknown message
