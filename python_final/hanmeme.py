import random

def random_img():
    imgur = ['https://i.imgur.com/121b5Ys.jpg', 'https://i.imgur.com/TlXoRef.jpg', 'https://i.imgur.com/4x5s5Cd.jpg', 'https://i.imgur.com/sBo6nMW.jpg', 'https://i.imgur.com/SRhVBZy.jpg', 'https://i.imgur.com/KRhR9RG.jpg', 'https://i.imgur.com/g53I8Wv.jpg', 'https://i.imgur.com/UEwBqOC.jpg', 'https://i.imgur.com/AIl5WcW.jpg', 'https://i.imgur.com/gnB0Jl2.jpg', 'https://i.imgur.com/43SXlW0.jpg', 'https://i.imgur.com/ACtDddL.jpg', 'https://i.imgur.com/v49xodl.jpg', 'https://i.imgur.com/JcOdzzc.jpg', 'https://i.imgur.com/QO2xl8H.jpg', 'https://i.imgur.com/7R2h8p9.jpg', 'https://i.imgur.com/tV5g2zb.jpg', 'https://i.imgur.com/kst62yu.jpg', 'https://i.imgur.com/zqj36in.jpg', 'https://i.imgur.com/BUUwDHY.jpg', 'https://i.imgur.com/rYtg4nH.jpg', 'https://i.imgur.com/DOpOaKI.jpg', 'https://i.imgur.com/82z6Opx.jpg', 'https://i.imgur.com/g5Fap3R.jpg', 'https://i.imgur.com/DTUmI2r.jpg', 'https://i.imgur.com/lFiF334.jpg', 'https://i.imgur.com/jUbMZv0.jpg', 'https://i.imgur.com/QCMsO25.jpg', 'https://i.imgur.com/zqPx8lg.jpg']
    r_img = random.randint(0,29)
    return imgur[r_img]

s = random_img()
print(s)