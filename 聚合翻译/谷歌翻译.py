import js2py,requests
string=input('输入字符串：')
js=js2py.EvalJs()
js.execute('function TL(a){var k="";var b=406644;var b1=3293161072;var jd=".";var $b="+-a^+6";var Zb="+-3^+b+-f";for(var e=[],f=0,g=0;g<a.length;g++){var m=a.charCodeAt(g);128>m?e[f++]=m:(2048>m?e[f++]=m>>6|192:(55296==(m&64512)&&g+1<a.length&&56320==(a.charCodeAt(g+1)&64512)?(m=65536+((m&1023)<<10)+(a.charCodeAt(++g)&1023),e[f++]=m>>18|240,e[f++]=m>>12&63|128):e[f++]=m>>12|224,e[f++]=m>>6&63|128),e[f++]=m&63|128)}a=b;for(f=0;f<e.length;f++)a+=e[f],a=RL(a,$b);a=RL(a,Zb);a^=b1||0;0>a&&(a=(a&2147483647)+2147483648);a%=1E6;return a.toString()+jd+(a^b)};function RL(a,b){var t="a";var Yb="+";for(var c=0;c<b.length-2;c+=3){var d=b.charAt(c+2),d=d>=t?d.charCodeAt(0)-87:Number(d),d=b.charAt(c+1)==Yb?a>>>d:a<<d;a=b.charAt(c)==Yb?a+d&4294967295:a^d}return a}')
tk=js.TL(string)
landata={'query':string}
lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
lan=lanhtml.json()['lan']
if lan=='zh':
    to='en'
else:
    to='zh-CN'
resp=requests.get('https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&pc=1&otf=1&ssel=0&tsel=0&kc=1&tk=%s&q=%s'%(to,tk,string))
result=resp.json()[0][0][0]
print(result)