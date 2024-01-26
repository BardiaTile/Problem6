class MrKrabs:
    def __init__(self, data):
        self.data = data

    def process_data(self):

        if self.data.startswith("m"):
            # Process Mr. Krabs data
            result = self.process_mr_krabs_data()
        elif self.data.startswith("sb"):
            # Process SpongeBob data
            result = self.process_spongebob_data()
        elif self.data.startswith("s") and self.data[1] != "b":
            # Process Squidward data
            result = self.process_squidward_data()
        elif self.data[-1]=="m":
            self.data=self.data[::-1]
            result = self.process_mr_krabs_data()
        elif self.data[-1]=="s" and self.data[-2]=="b":
            self.data=self.data[::-1]
            result = self.process_spongebob_data()
        elif self.data[-1]=="s" and self.data[-2]!="b":
            self.data=self.data[::-1]
            result = self.process_squidward_data()
        else:
            result = "invalid input"

        return result

    def process_mr_krabs_data(self):
        result = self.data.replace("tt", "o")
        tee=self.data[:10].replace("tt","o")
        return result+tee

    def process_spongebob_data(self):
        def mergeSort(arr):
         if len(arr) > 1:
 
            mid = len(arr)//2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]
 
            mergeSort(sub_array1)
            mergeSort(sub_array2)
         
            i = j = k = 0
 
            while i < len(sub_array1) and j < len(sub_array2):
                if sub_array1[i] < sub_array2[j]:
                    arr[k] = sub_array1[i]
                    i += 1
                else:
                    arr[k] = sub_array2[j]
                    j += 1
                k += 1
 
            while i < len(sub_array1):
                arr[k] = sub_array1[i]
                i += 1
                k += 1
 
            while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1
 

        def sort_dna_length(dna_sequence):
           length_str = list(str(len(dna_sequence)))
           jeff = [int(length_str[i]) for i in range(len(length_str))]
 
           mergeSort(jeff)

           sorted_length =""
           for i in range(len(jeff)):
            if i==0:
             sorted_length+=f"{jeff[i]+1}"
            else:
             sorted_length+=f"{jeff[i]}"

           return sorted_length
        return sort_dna_length(self.data)

    def process_squidward_data(self):
        result = ""
        fllag=False
        i = 0
        ffs=0
        while i < len(self.data):
            count = 1
            if fllag==False and self.data[i]=="x":
                    ffs+=i
                    fllag=True
            while i + count < len(self.data) and self.data[i] == self.data[i + count]:
                count += 1
                if count+1==4:
                    break

            if count >= 3:
                result += "(0_0)"
                i += count
            else:
                result += self.data[i]
                i += 1
        if fllag==True:
            result+=f"{ffs}"
        return result
input_data = input()

mr_krabs = MrKrabs(input_data)

result = mr_krabs.process_data()
print(result)
