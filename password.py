###############################
# probelm no. - 05          #
# The variant of passwords   #
# password.py               #
##############################
class Password_Variant:
    def __init__(self,testcase):
        self.testcase=testcase
    def process_testcase(self):
        for i in range (self.testcase):
            pwd_len =  int(input())
            #print(pwd_len)
            details = input()
            details=details.split()
            details = [int(num) for num in details]
            #print(details)
            password_org = input()
            #print(password_org)
            #pwd_len =  details[0]
            count_0 = password_org.count('0')
            #count_0_req = details[1]
            count_0_req = details[0]
            count_1 = password_org.count('1')
            #count_1_req = details[2]
            count_1_req = details[1]
            password_list = [char for char in password_org]
            replacement = 0
            for i in range (pwd_len):
                if(password_list[i] == '0' and count_0_req >=1):
                    count_0 = count_0 -1
                    count_0_req = count_0_req -1
                elif(password_list[i] == '1' and (count_1>count_1_req and count_0_req> count_0)):
                    password_list[i] = '0'
                    count_1 = count_1 -1
                    count_0_req = count_0_req-1
                    replacement = replacement +1
                elif (password_list[i] == '1' and count_1_req >=1):
                    count_1 = count_1 -1
                    count_1_req = count_1_req -1
                elif (count_0_req > 0 or count_1_req > 0 ):
                    if(count_0_req > count_0 ):
                        password_list[i] = '0'
                        replacement = replacement +1
                        count_0_req = count_0_req -1
                    elif(count_1_req > count_1  ):
                        password_list[i] = '1'
                        replacement = replacement +1
                        count_1_req = count_1_req -1
                elif (count_0_req == 0 or count_1_req == 0):
                    if (password_list[i] == '0' or password_list[i] == '1'):
                        password_list[i] = '2'
                        replacement = replacement +1

        # Writing output to STDOUT
            print(replacement)
            password_converted = ''.join(password_list)
            print(password_converted)

# Reading input from STDIN 
testcase = int(input())
#print(testcase)
password_variant=PasswordVariant(testcase)
password_variant.process_testcase()
         
