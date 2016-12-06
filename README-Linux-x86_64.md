### Electrum-ion - lightweight multi-coin client
Electrum-ion provides a basic SPV wallet for Dashpay. It is a BIP-0044-compliant wallet based on the original Electrum for Bitcoin. This Electrum-ion client uses Electrum servers to retrieve necessary blockchain headaer & transaction data, so no "Electrum-ion server" is necessary.

Because of the Simplified Payment Verification nature of the wallet, services requiring Masternode communications, such as DarkSend and InstantX are not available.

Homepage: https://ionomy.com/electrum-ion




1. ELECTRUM_ION ON LINUX
----------------------

 - Installer package is provided at https://ionomy.com/electrum-ion
 - To download and use:
    ```
    cd ~
    wget https://ionomy.com/electrum-ion/releases/v2.4.1/Electrum-ion-2.4.1-Linux_x86_64.tgz
    tar -xpzvf Electrum-ion-2.4.1-Linux_x86_64.tgz
    cd Electrum-ion-2.4.1
    ./electrum-ion_x86_64.bin
    ```


Once successfully installed simply type
   ```
   electrum-ion
   ```
   Your wallets will be located in /home/YOUR_LOGIN_NAME/.electrum-ion/wallets

Installation on 32bit machines is best achieved via github master or TAGGED branches

2. HOW OFFICIAL PACKAGES ARE CREATED
------------------------------------

See contrib/electrum-ion-release/README.md for complete details on mazaclub release process

