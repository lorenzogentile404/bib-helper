# bib-helper

A simple Python script to run queries on `.bib` files.

Here is an example of usage:

```console
user@host:~$ python3 bib_helper.py 
Insert search terms: goldwasser micali rivest 88
...
@InProceedings{ISC:PenBoyDaw05,
  author =       "Kun Peng and
                  Colin Boyd and
                  Ed Dawson",
  title =        "A Multiplicative Homomorphic Sealed-Bid Auction Based on {Goldwasser}-{Micali} Encryption",
  pages =        "374--388",
  editor =       isc05ed,
  booktitle =    isc05name,
  volume =       isc05vol,
  address =      isc05addr,
  month =        isc05month,
  publisher =    iscpub,
  series =       mylncs,
  year =         2005,
}

Relevance: 3

@Article{GolMicRiv88,
  author =       "Shafi Goldwasser and
                  Silvio Micali and
                  Ronald L. Rivest",
  title =        "A Digital Signature Scheme Secure Against Adaptive Chosen-message Attacks",
  journal =      siamjc,
  month =        apr,
  year =         1988,
  pages =        "281--308",
  volume =       17,
  number =       2,
}

Relevance: 4

Number of results: 2866

```
