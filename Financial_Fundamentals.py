import yfinance as yf
import requests

symbol_NSE = input('Enter ticker Name here -: ')
count = 0
x = yf.Ticker(f'{symbol_NSE}.NS').info
print(x)
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
session.get("http://nseindia.com")
data = session.get(f"https://www.nseindia.com/api/quote-equity?symbol={symbol_NSE}").json()

# general data and low and highs
print(f"symbol/ticker name -- {data['info']['symbol']}")
print(f"Company Name --  {data['info']['companyName']}")
print(f"Stock Industry -- {data['info']['industry']}")
print(f"Stock Series -- {data['metadata']['series']}")
print(f"listing date -- {data['metadata']['listingDate']}")
print(f"Sector Index -- {data['metadata']['pdSectorInd']}")
print(f" last price -- {data['priceInfo']['lastPrice']}")
print(f" change in last day -- {round(data['priceInfo']['change'],3)}")
print(f" change in percent change  -- {round(data['priceInfo']['pChange'],6)}")
print(f" previous close -- {data['priceInfo']['previousClose']}")
print(f" Market cap -- {x['marketCap']}")
print(f" Current price -- {x['currentPrice']}")
print(f" 52W high -- {x['fiftyTwoWeekHigh']}")
print(f" 52E Low -- {x['fiftyTwoWeekLow']}")
print(f" 50 day average -- {x['fiftyDayAverage']}")
print(f" 200 day average -- {x['twoHundredDayAverage']}")
print(f" Shares Outstanding -- {x['sharesOutstanding']}")
print(f" Float Shares -- {x['floatShares']}")
print(f" Implied shares Outstanding -- {x['impliedSharesOutstanding']}")
print(f" percent shares holded by Insiders -- {x['heldPercentInsiders']}")
print(f" percent shares held by instutions -- {x['heldPercentInstitutions']}")

#cash values
print(f" Total Cash -- {x['totalCash']}")
print(f" Total Cash per share -- {x['totalCashPerShare']}")
print(f" Total Debt -- {x['totalDebt']}")
print(f" Total Revenue -- {x['totalRevenue']}")
print(f" Total free cash flow -- {x['freeCashflow']}")
print(f" operating cash flow -- {x['operatingCashflow']}")

#volumes
print(f" volume -- {x['volume']}")
print(f" regular market volume -- {x['regularMarketVolume']}")
print(f" average volume -- {x['averageVolume']}")
print(f" 10 day average volume -- {x['averageVolume10days']}")
print(f" average daily 10 day volume -- {x['averageDailyVolume10Day']}")


#profitability ratios
print(f" ROE -- {x['returnOnEquity']}")
print(f" ROA -- {x['returnOnAssets']}")
print(f" Op cash flow -- {x['operatingCashflow']}")
print(f" EPS -- {x['trailingEps']}")
print(f" predicted EPS -- {x['forwardEps']}")
print(f" Beta -- {x['beta']}")
print(f" Profit margins -- {x['profitMargins']}") #net profit margin
print(f" Debt to eqity -- {x['debtToEquity']}")
print(f" revenue per share -- {x['revenuePerShare']}")
print(f" Earnings Growth -- {x['earningsGrowth']}")
print(f" Revenue Growth -- {x['revenueGrowth']}")
print(f" Gross Margins -- {x['grossMargins']}")
print(f" Ebitda Margins -- {x['ebitdaMargins']}")
print(f" Operating Margins -- {x['operatingMargins']}")


#dividend ratios
print(f" Dividend Yeild -- {round(x['dividendYield'],3)}")
print(f" Five year avg dividend yeild -- {round(x['fiveYearAvgDividendYield'],3)}")
print(f" payout ratio -- {round(x['payoutRatio'],3)}")

#valuation ratios
print(f" Stock sector PE -- {round(data['metadata']['pdSectorPe'],2)}")
print(f" Face value -- {round(data['securityInfo']['faceValue'],2)}")
print(f" Price to book value -- {round(x['priceToBook'],2)}")
print(f" current PE -- {round(x['trailingPE'],2)}")
print(f" Predicted PE -- {round(x['forwardPE'],2)}")
print(f" PEG ratio -- {round(x['pegRatio'],2)}")
print(f" Editda -- {x['ebitda']}")
print(f" Enterprice to revneue -- {round(x['enterpriseToRevenue'],2)}")
print(f" Enterprise to editda -- {round(x['enterpriseToEbitda'],2)}")
print(f" Price to sales ratio -- {round(x['priceToSalesTrailing12Months'],2)}")

#operational ratios

print(f" Quick ratio -- {round(x['quickRatio'],2)}")
print(f" current Ratio -- {round(x['currentRatio'],2)}")


ROE = x['returnOnEquity']
ROA = x['returnOnAssets']
Cash_per_share = x['totalCashPerShare']
profit_margin = x['profitMargins']
PE = round(x['trailingPE'],2)
PB = round(x['priceToBook'],2)
Quick_ratio = round(x['quickRatio'],2)
current_Ratio = round(x['currentRatio'],2)
PEG_Ratio = round(x['pegRatio'],2)
debt_to_eqity= x['debtToEquity']
if ROE > .25:
    count = count + 1
if ROA > .15:
    count = count + 1
if Cash_per_share > 0:
    count = count + 1
if profit_margin > 0:
    count = count+ 1
if PE < 30:
    count = count + 1
if PB < 3:
    count = count +1
if Quick_ratio > 1 :
    count = count + .5
if current_Ratio > 2:
    count = count + .5
if PEG_Ratio < 1.5:
    count = count + 1
if debt_to_eqity > 3:
    count = count + 1

if count > 6:
    print('Fundamentally strong')

import yahoo_fin.stock_info as yf
# import requests
# from bs4 import BeautifulSoup
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
# url = "https://ticker.finology.in/company/TATASTEEL"
# response = requests.get(url)
# response = response.content
# soup = BeautifulSoup(response, 'html.parser')
#
# h1_span = soup.find('span', {'id': 'mainContent_ltrlCompName'})
#
# h1_text = h1_span.text.strip()
#
# div = soup.find('div', {'class': 'col-6 col-md-4 compess'})
#
# print(h1_text)
# div = div.text.strip()
# print(div)
# import requests
#
# url = "https://alpha-vantage.p.rapidapi.com/query"
#
# querystring = {"function":"GLOBAL_QUOTE","symbol":"TCS","datatype":"json"}
#
# headers = {
# 	"X-RapidAPI-Key": "4bcf85c806msh704da1500012eacp10c8b7jsn35042e626f65",
# 	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
