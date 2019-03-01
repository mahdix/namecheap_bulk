# Namecheap Bulk Reuqeast

A simple script to register a list of domains. 

## To start

1. Enter required domains you want to register in `domains.txt`
2. Run `./run.sh domains.txt`
3. The script will try to register domains in the order spceified in the input file.
4. Successfully registered domains will be written to `success.txt`


## Modifications you should/can make:

1. In the `run.py` you should set `Sandbox` to `False` if you want to use your real account.
2. Make sure you have enabled Namecheap API and whitelisted your server's IP address there.
3. Put your API key and IP address in `run.py`
4. Make sure provided values for domain registration are correct in `run.py` (address, phone number, ...)

