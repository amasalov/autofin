
import json
import csv



def main():
    print("---telegram json converter to csv for Family Finance channel---")
    # Opening JSON file
    with open("./sept1-sept2.json") as json_file:
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
            norm_msg['date'] = list[i]['date'].split('T')[0] #need to remove time, just keep the date or get the date from unixtimestamp
           
            norm_msg['from'] = list[i]['from']
            #normolized_msg['text'] = list[i]['text_entities'][0]['text'] #need to make a loop and stich a string
            norm_text = ""
            print("list[i]['text_entities']",list[i]['text_entities'])
            for t in list[i]['text_entities']:
                norm_text += t['text']
                print(norm_text)
            norm_msg['text'] = norm_text
            norm_list.append(norm_msg)

        


        #try converting telegram json to one level dict, so i can save as csv

    #print(type(data))
    print(norm_list)
    return(norm_list)

   #save this json as is in csv


    #with open("./output_csv", "w", newline="", encoding="utf-8") as csv_file:
    #    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
     #   writer.writeheader()
    #   writer.writerows(data)




main()


