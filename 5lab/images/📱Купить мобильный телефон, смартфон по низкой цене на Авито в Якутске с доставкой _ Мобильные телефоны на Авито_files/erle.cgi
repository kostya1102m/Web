
(function (ph){
try{
var A = self['DSPCounter' || 'AdriverCounter'],
	a = A(ph);
a.reply = {
ph:ph,
rnd:'378025',
bt:62,
sid:223878,
pz:0,
sz:'%2f',
bn:0,
sliceid:0,
netid:0,
ntype:0,
tns:0,
pass:'',
adid:0,
bid:2864425,
geoid:156,
cgihref:'//ad.adriver.ru/cgi-bin/click.cgi?sid=223878&ad=0&bid=2864425&bt=62&bn=0&pz=0&xpid=DzFgQybofEVYuqI_pJVc6SpfZ1VV0m4CZa-_H-7LIBz2rX2TQTWAtHcTHxYjjHgISexKJ79wqFarDXw&ref=https:%2f%2fwww.avito.ru%2f&custom=157%3Dundefined%3B158%3D32rpu1ka.lehfym.1jz3oi58hpgw0%3B10%3Dundefined%3B206%3DDSPCounter',
target:'_blank',
width:'0',
height:'0',
alt:'AdRiver',
mirror:A.httplize('//masterh7.adriver.ru'), 
comp0:'0/script.js',
custom:{"10":"undefined","157":"undefined","158":"32rpu1ka.lehfym.1jz3oi58hpgw0","206":"DSPCounter"},
cid:'',
uid:0,
xpid:'DzFgQybofEVYuqI_pJVc6SpfZ1VV0m4CZa-_H-7LIBz2rX2TQTWAtHcTHxYjjHgISexKJ79wqFarDXw'
}
var r = a.reply;

r.comppath = r.mirror + '/images/0002864/0002864425/' + (/^0\//.test(r.comp0) ? '0/' : '');
r.comp0 = r.comp0.replace(/^0\//,'');
if (r.comp0 == "script.js" && r.adid){
	A.defaultMirror = r.mirror; 
	A.loadScript(r.comppath + r.comp0 + '?v' + ph) 
} else if ("function" === typeof (A.loadComplete)) {
   A.loadComplete(a.reply);
}
}catch(e){} 
}('0'));
