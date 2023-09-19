skumriq_price = float(input())
caca_price = float(input())
palamud_kilos = float(input())
safrid_kilos = float(input())
midi_kilos = int(input())

palamud_price = skumriq_price + skumriq_price * 0.6
safrid_price = caca_price + caca_price * 0.8
midi_price = 7.50

total_price = (palamud_price * palamud_kilos) + (safrid_price * safrid_kilos) + (midi_price * midi_kilos)
print("%.2f" % total_price)