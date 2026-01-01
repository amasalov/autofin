
import json
import csv
from script import return_number

# [ ] assign #hashtags based on hashtags
# [ ] if several numbers in string should be two different rows and hashtag #split
# [ ] assign #hashtags based on text 

#return_first_int_from_string



def main():
    print("---telegram json converter to csv for Family Finance channel---")
    # Opening JSON file
    with open("sept01-sept30.json") as json_file:
        data = json.load(json_file)

        list = []
        norm_list = []
        normolized_msg = {}
        del data['name']
        del data['type']
        del data['id']

        list = data["messages"]
        
        for i in range (len(list)):
            norm_msg = {}
            if(list[i]['type'] == "message"):
                norm_msg['id'] = list[i]['id']
                norm_msg['date'] = list[i]['date'].split('T')[0]
                norm_msg['from'] = list[i]['from']
                norm_text = ""
                #print("list[i]['text_entities']",list[i]['text_entities'])
                for t in list[i]['text_entities']:
                    norm_text += t['text']
                
                norm_msg['text'] = norm_text
                print(norm_msg['date'], norm_msg['text'])
                norm_msg['sum'] = 0
                norm_msg['sum'] = return_number(norm_text)
                print("sum", norm_msg['sum'])
                #take first integer in text and assign it's value to norm_msg['sum']. If more numbers in text that need to create a special #hashtag split
                norm_msg['hashtag'] = ""
                norm_list.append(norm_msg)

        


        


    #print(norm_list)
    return(norm_list)

   #save this json as is in csv


    #with open("./output_csv", "w", newline="", encoding="utf-8") as csv_file:
    #    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
     #   writer.writeheader()
    #   writer.writerows(data)




main()


