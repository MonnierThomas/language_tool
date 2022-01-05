import argparse

from src.correction import Correction

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Choose between sentence or batch correction')
    parser.add_argument('--sentence', nargs='+', help='enter the sentence you want to correct')
    parser.add_argument('--batch', nargs='+', help='enter the path of the batch you want to correct')
    parser.add_argument('--full_json', help='enter True to print the full JSON returned by LanguageTool for every sentence')
    args = parser.parse_args()
    
    full_json = False
    if args.full_json != None:
        try:
            if args.full_json.lower() == 'true':
                full_json = True
        except:
            print('The value of full_json is not equal to True')

    if args.sentence != None:
        for sentence in args.sentence:
            text = "text="+sentence
            correction = Correction(text, full_json)
            correction.get_correction()
            correction.display_correction()
            correction.get_errors()
            correction.display_errors()
    
    if args.batch != None:
        for batch in args.batch:
            with open(batch) as f:
                sentences = f.read().splitlines()
                for sentence in sentences:
                    text = "text="+sentence
                    correction = Correction(text, full_json)
                    correction.get_correction()
                    correction.display_correction()
                    correction.get_errors()
                    correction.display_errors()