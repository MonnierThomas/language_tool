# LanguageTool API

> An easy, fast and free way to use LanguageTool API

This repository provides an easy way to use the API of LanguageTool for Grammatical Error Correction (FREE VERSION). Thanks to LanguageTool, it is now amazingly simple to correct sentences and batches with low effort and tremendous results.

# Table of contents

- [LanguageTool](#languagetool)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Docker](#docker)
- [References](#references)

# LanguageTool
LanguageTool is an Open Source proofreading software for English, French, German, Polish, Russian, and more than 20 other languages. It finds many errors that a simple spell checker cannot detect.

- [Jobs at LanguageTool](https://languagetool.org/careers)
- [How to run your own LanguageTool server](https://dev.languagetool.org/http-server)
- [HTTP API documentation](https://languagetool.org/http-api/swagger-ui/#!/default/post_check)
- [How to use LanguageTool's public server via HTTP](https://dev.languagetool.org/public-http-api)
- [How to use LanguageTool from Java](https://dev.languagetool.org/java-api) (Javadoc)

For more information, please see LanguageTool's homepage at [https://languagetool.org](https://languagetool.org/), [this README](https://github.com/languagetool-org/languagetool/blob/master/languagetool-standalone/README.md), and [CHANGES](https://github.com/languagetool-org/languagetool/blob/master/languagetool-standalone/CHANGES.md).

LanguageTool is freely available under the LGPL 2.1 or later.

For this project, LanguageTool offer a simple HTTPS REST-style service that anybody can use to check texts with LanguageTool. The only public endpoint is the following one - do not send your requests to any other endpoints you might find in the homepage’s HTML code or elsewhere -:

[https://api.languagetool.org/v2/check](https://api.languagetool.org/v2/check)

When using it, please keep the following rules in mind:

- Do not send automated requests. For that, set up your own instance of LanguageTool or get an account for Enterprise use.
- Only send POST requests, not GET requests.
- Access is currently limited to:
> 20 requests per IP per minute (this is supposed to be a peak value - don’t constantly send this many requests or LanguageTool would have to block you)

> 75KB text per IP per minute

> 20KB text per request

> Only up to 30 misspelled words will have suggestions

This is a free service, thus there are no guarantees about performance or availability. The limits may change anytime.

The LanguageTool version installed may be the latest official release or some snapshot. LanguageTool will simply deploy new versions, thus the behavior will change without any warning.

# Installation

After cloning the project,

```
pip3 install requirements.txt
```

Export the project to your PYTHONPATH.

# Quick start

With LanguageTool, you can use either correct sentences or batches.

```
usage: main.py [-h] [--sentence SENTENCE [SENTENCE ...]] [--batch BATCH [BATCH ...]] [--full_json FULL_JSON]

Choose between sentence or batch correction

optional arguments:
  -h, --help                            show this help message and exit
  --sentence SENTENCE [SENTENCE ...]    enter the sentence you want to correct
  --batch BATCH [BATCH ...]             enter the path of the batch you want to correct
  --full_json FULL_JSON                 enter True to print the full JSON returned by LanguageTool for every sentence
```
  
Examples: 
  
```
python3 src/main.py --sentence 'I have many dog' 'I couldnt tell there freinds'
```
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1105  100  1071  100    34   5124    162 --:--:-- --:--:-- --:--:--  5261
Sentence:  I have many dog
Errors detected:
length:  8
offset:  7
value of replacement: many dogs
#############
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2265  100  2218  100    47  11432    242 --:--:-- --:--:-- --:--:-- 11735
Sentence:  I couldnt tell there freinds
Errors detected:
length:  7
offset:  2
value of replacement: couldn't
#############
length:  5
offset:  15
value of replacement: their
#############
length:  7
offset:  21
value of replacement: friends
#############
```

-------

```
python3 src/main.py --sentence 'I have many dog.' --full_json True
```

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1108  100  1073  100    35   4990    162 --:--:-- --:--:-- --:--:--  5129
Full JSON:
{
    "language": {
        "code": "en-US",
        "detectedLanguage": {
            "code": "en-US",
            "confidence": 0.528,
            "name": "English (US)"
        },
        "name": "English (US)"
    },
    "matches": [
        {
            "context": {
                "length": 8,
                "offset": 7,
                "text": "I have many dog."
            },
            "contextForSureMatch": 10,
            "ignoreForIncompleteSentence": true,
            "length": 8,
            "message": "Possible agreement error. The noun \u2018dog\u2019 seems to be countable; consider using: \u201cmany dogs\u201d.",
            "offset": 7,
            "replacements": [
                {
                    "value": "many dogs"
                }
            ],
            "rule": {
                "category": {
                    "id": "GRAMMAR",
                    "name": "Grammar"
                },
                "description": "Possible agreement error: 'many/several/few' + singular countable noun",
                "id": "MANY_NN",
                "isPremium": false,
                "issueType": "grammar",
                "sourceFile": "grammar.xml",
                "subId": "1"
            },
            "sentence": "I have many dog.",
            "shortMessage": "Grammatical problem",
            "type": {
                "typeName": "Other"
            }
        }
    ],
    "software": {
        "apiVersion": 1,
        "buildDate": "2022-01-03 19:40:26 +0000",
        "name": "LanguageTool",
        "premium": true,
        "premiumHint": "You might be missing errors only the Premium version can find. Contact us at support<at>languagetoolplus.com.",
        "status": "",
        "version": "5.7-SNAPSHOT"
    },
    "warnings": {
        "incompleteResults": false
    }
}
#############
Sentence:  I have many dog.
Errors detected:
length:  8
offset:  7
value of replacement: many dogs
#############
```

-------

To use `--batch` argparse, do the following:
```
python3 src/main.py --batch path_of_batch.csv
```

Accepted batch format: `.txt`, `.csv`

A file `output.json` will be created, containing a JSON in format (text, edits) which can then be converted into M2 format very easily.
  
# Docker

It's now a possibility to use Docker to run LanguageTool.

Follow these steps in order to build:
- `docker build . -t language_tool --network=host  # it will build the docker image`
  
Then you can do whatever you want (from correcting sentences to batches, and returning the full JSON):
Example:
- `docker run language_tool:latest --sentence 'I have many dog.'`
- `docker run language_tool:latest --sentence 'I have many dog' --full_json True`
- `docker run language_tool:latest --batch to_correct.csv`

# References

- [LanguageTool](https://languagetool.org/)
- [How to run your own LanguageTool server](https://dev.languagetool.org/http-server)
- [HTTP API documentation](https://languagetool.org/http-api/swagger-ui/#!/default/post_check)
- [How to use LanguageTool's public server via HTTP](https://dev.languagetool.org/public-http-api)
