import MetaTrader5 as mt5
import pandas as pd 

mt5.initialize()

def PegaInfoAtivo(ativo):
    # mt5.symbol_select(ativo, True)
    infoAtivo = mt5.symbol_info(ativo)
    priceAsk = mt5.symbol_info_tick(ativo).ask
    priceBid = mt5.symbol_info_tick(ativo).bid
    priceLast = mt5.symbol_info_tick(ativo).last
    
    print(ativo, infoAtivo.option_strike, priceBid, priceAsk, priceLast)

    ativo = ['VALEF114', 'VALEF121', 'VALEF877', 'VALEG108', 'VALEG972']

    for i in range(len(ativo)):
    PegaInfoAtivo(ativo[i])

    mt5.shutdown()