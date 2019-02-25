from flask import Flask,request
from random import *
from Crypto.Cipher import DES3
from Crypto import Random

key = b'0101011111001100'
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)

app = Flask(__name__)
@app.route("/",methods=["POST"])
def functi():
	if request.method=="POST":
		key=str(request.form.get('key'))
		arr=[]
		for i in range(len(key)):
			arr.append(i)
		plaintext=' '.join(arr)
		encrypted_text = cipher_encrypt.encrypt(plaintext)
		cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv)
		final=cipher_decrypt.decrypt(encrypted_text)
		return final
		# return render_template('verify2.html', finalk=final)

if __name__ == '__main__':
	app.run(debug=True)
