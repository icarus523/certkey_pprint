import subprocess
import glob
import logging
import pprint

# Configure logging to file and format
logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s - %(levelname)-8s %(message)s',
        datefmt='%d-%m-%y %H:%M',
        filename='cert_info.log',
        filemode='w')

def decode_x509_certificate(file_list): 
	for f in file_list:
		logging.getLogger().info("Processing: " + f)
		cert_txt = subprocess.run(["openssl","x509","-text","-noout","-in", f],stdout=subprocess.PIPE).stdout
		logging.getLogger().info(cert_txt.decode("utf-8"))

def decode_key(key_list): 
	for k in key_list: 
		logging.getLogger().info("Processing: " + k)
		cert_txt = subprocess.run(["openssl","rsa","-in",k,"-text","-noout"],stdout=subprocess.PIPE).stdout
		logging.getLogger().info(cert_txt.decode("utf-8"))		

logging.getLogger().info("Generate Details for all Certificates")
certs = glob.glob('*.crt')
decode_x509_certificate(certs)

logging.getLogger().info("Generate Details for all Keys")
keys = glob.glob('*.key')
decode_key(keys)
