import json

def billzer():
    n = int(input("Enter n: "))

    data = {}

    data["friendCount"] = n

    total = 0
    data['friends'] = []
    friends = data['friends']

    for i in range(0, n):
        name = input("Enter name: ")
        amount = float(input("Enter amount: "))
        friends.append({})
        friends[i]['name'] = name
        friends[i]['amountPaid'] = amount

        total += friends[i]['amountPaid']

        friends[i]['toReceive'] = False
        friends[i]['toGive'] = False

        friends[i]['amountGive'] = 0
        friends[i]['amountReceive'] = 0

        friends[i]['transaction'] = {'details': []}

    money = []

    costPerPerson = total/n

    data['costPerPerson'] = costPerPerson

    data['totalCost'] = total

    for i in friends:
        if i['amountPaid'] > costPerPerson:
            i['toReceive'] = True
            i['amountReceive'] = i['amountPaid'] - costPerPerson

            money.append(i['amountReceive']) 

        elif i['amountPaid'] < costPerPerson:

            i['toGive'] = True
            i['amountGive'] = costPerPerson - i['amountPaid']

            money.append(-i['amountGive'])

        else:
            money.append(0)

    tid = 0

    for i in range(0, n):
        if money[i] < 0:
            for j in range(0, n):
                if i==j:
                    continue
                if(money[j] > 0):
                    tid+=1
                    send = {'transactionId': tid, 'receiveFrom': None, 'sendTo': friends[j]['name']}
                    receive = {'transactionId': tid, 'sendTo': None, 'receiveFrom': friends[i]['name']}
                    if(money[j] > -(money[i])):
                        send['amount'] = -money[i]
                        receive['amount'] = -money[i]
                        friends[i]['transaction']['details'].append(send)
                        friends[j]['transaction']['details'].append(receive)
                        money[j] = money[j] + money[i]
                        money[i] = 0
                    elif(-(money[i]) > money[j]):
                        send['amount'] = money[j]
                        receive['amount'] = money[j]
                        friends[i]['transaction']['details'].append(send)
                        friends[j]['transaction']['details'].append(receive)
                        money[i] = money[i] + money[j]
                        money[j] = 0
                    else:
                        send['amount'] = money[j]
                        receive['amount'] = money[j]
                        friends[i]['transaction']['details'].append(send)
                        friends[j]['transaction']['details'].append(receive)
                        money[i] = 0
                        money[j] = 0
        
    return data

if __name__ == "__main__":
    data = billzer()

    with open("dataSet.json", "w") as outfile:
        json.dump(data, outfile, indent=2)
    