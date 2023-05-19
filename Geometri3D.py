import math

def LuasPermukaanKubus(s):
    return 6*s**2

def VolumeKubus(s):
    return s**3

def LuasPermukaanBalok(p,l,t):
    return 2(p*l)+2(p*t)+2(l*t)

def VolumeBalok(p,l,t):
    return p*l*t

def LuasPermukaanPrismaSegitiga(s1,s2,s3,Tprisma,a,t):
    return (s1+s2+s3)*Tprisma + a*t

def VolumePrismaSegitiga(a,t,Tprisma):
    return 1/2*a*t*Tprisma

def LuasPermukaanTabung(r,T):
    return 2*math.pi*r*T

def VolumeTabung(r,T):
    return math.pi*T*r**2

def LuasPermukaanKerucut(r,s):
    return math.pi*r(s+r)

def VolumeKerucut(r,T):
    return 1/3*math.pi*T*r**2

def LuasPermukaanBola(r):
    return 4*math.pi*r**2

def VolumeBola(r):
    return 4/3*math.pi*r**3