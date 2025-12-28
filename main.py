
import json
import csv
import sys


def main():
    print("---telegram json converter to csv for Family Finance channel---")
    # Opening JSON file
    with open("./sept1-sept2.json") as json_file:
        data = json.load(json_file)

        list = []
        normolized_list = []
        normolized_msg = {}
        del data['name']
        del data['type']
        del data['id']

        list = data["messages"]
        
        for i in range (len(list)):
            normolized_msg = {}
            normolized_msg['date'] = list[i]['date']
            normolized_msg['from'] = list[i]['from']
            normolized_msg['text'] = list[i]['text_entities'][0] #need to make a loop and stich a string
            normolized_list.append(normolized_msg)

        


        #try converting telegram json to one level dict, so i can save as csv

    #print(type(data))
    print(normolized_list)

   #save this json as is in csv


    #with open("./output_csv", "w", newline="", encoding="utf-8") as csv_file:
    #    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
     #   writer.writeheader()
    #   writer.writerows(data)




main()


