### Electrum-ion - lightweight multi-coin client

Electrum-ion provides a basic SPV wallet for Dashpay. It is a BIP-0044-compliant wallet based on the original Electrum for Bitcoin. This Electrum-ion client uses Electrum servers to retrieve necessary blockchain headaer & transaction data, so no "Electrum-ion server" is necessary.

Because of the Simplified Payment Verification nature of the wallet, services requiring Masternode communications, such as DarkSend and InstantX are not available.

Homepage: https://dashpay.io/electrum-ion

1. Download the .dmg from https://dashpay.io/electrum-ion
2. Open .dmg in Finder
3. Double Click Electrum-ion.pkg
4. Follow instructions to install Electrum-ion

Electrum-ion will be installed by default to /Applications

Your Wallets will be stored in /Users/YOUR_LOGIN_NAME/.electrum-ion/wallets

### KNOWN ISSUES



2. HOW OFFICIAL PACKAGES ARE CREATED
------------------------------------

contrib/mazaclub-release

 
The 'build' script will perform all the necessary tasks to 
create a release from release-tagged github sources

If all runs correctly, you''ll find a release set in the 
contrib/electrum-ion-release/releases directory, complete with 
md5/sha1 sums, and gpg signatures for all files. 

Additional documentation is provided in the README in that dir.
Official Releases are created with a single OSX machine, boot2docker vm and docker

