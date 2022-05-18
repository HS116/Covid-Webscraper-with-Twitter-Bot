import json

#Serialize json from dictionaries developed from web scraping
#TODO: store the change in indian covid cities covid data in json file. 
#Issue is that the up arrow is represented as "/u2191", and we need to remove that, could u lamda function for that

def create_json_file(data, file_name):

    #Add a time stamp
    from datetime import datetime
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y %H:%M:%S")

    data = convert_text_val_of_dict(data)
    with open(f'jsonData/{file_name}_{timestamp}.json', 'w') as f:
        json.dump(data, f, indent=4)

    
    

def convert_text_to_int(text):
    #remove commas and the '\u2191' which represents the up arrow character
    return int(text.replace(',', '').replace('\u2191', ''))

def convert_text_val_of_dict(dictionary):
    #convert the string values of each dictionary to integer to make it easier for future data analysis
    #using dict() and list comprehension    
    return dict([key, convert_text_to_int(value)] for key, value in dictionary.items())

