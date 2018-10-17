import json
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os
import re
FJoin = os.path.join
class Process_file:
	def readFile(self,fileName):
		data_result = []
		with open(fileName) as jsondata:
			datas = json.load(jsondata)
			print(datas[0])
			print(type(datas))
		return datas

	def replaceUnicode(self, str):
		str = str.replace("\u0065\u0309", "\u1EBB")
		str = str.replace("\u0065\u0301", "\u00E9")
		str = str.replace("\u0065\u0300", "\u00E8")
		str = str.replace("\u0065\u0323", "\u1EB9")
		str = str.replace("\u0065\u0303", "\u1EBD")
		str = str.replace("\u00EA\u0309", "\u1EC3")
		str = str.replace("\u00EA\u0301", "\u1EBF")
		str = str.replace("\u00EA\u0300", "\u1EC1")
		str = str.replace("\u00EA\u0323", "\u1EC7")
		str = str.replace("\u00EA\u0303", "\u1EC5")
		str = str.replace("\u0079\u0309", "\u1EF7")
		str = str.replace("\u0079\u0301", "\u00FD")
		str = str.replace("\u0079\u0300", "\u1EF3")
		str = str.replace("\u0079\u0323", "\u1EF5")
		str = str.replace("\u0079\u0303", "\u1EF9")
		str = str.replace("\u0075\u0309", "\u1EE7")
		str = str.replace("\u0075\u0301", "\u00FA")
		str = str.replace("\u0075\u0300", "\u00F9")
		str = str.replace("\u0075\u0323", "\u1EE5")
		str = str.replace("\u0075\u0303", "\u0169")
		str = str.replace("\u01B0\u0309", "\u1EED")
		str = str.replace("\u01B0\u0301", "\u1EE9")
		str = str.replace("\u01B0\u0300", "\u1EEB")
		str = str.replace("\u01B0\u0323", "\u1EF1")
		str = str.replace("\u01B0\u0303", "\u1EEF")
		str = str.replace("\u0069\u0309", "\u1EC9")
		str = str.replace("\u0069\u0301", "\u00ED")
		str = str.replace("\u0069\u0300", "\u00EC")
		str = str.replace("\u0069\u0323", "\u1ECB")
		str = str.replace("\u0069\u0303", "\u0129")
		str = str.replace("\u006F\u0309", "\u1ECF")
		str = str.replace("\u006F\u0301", "\u00F3")
		str = str.replace("\u006F\u0300", "\u00F2")
		str = str.replace("\u006F\u0323", "\u1ECD")
		str = str.replace("\u006F\u0303", "\u00F5")
		str = str.replace("\u01A1\u0309", "\u1EDF")
		str = str.replace("\u01A1\u0301", "\u1EDB")
		str = str.replace("\u01A1\u0300", "\u1EDD")
		str = str.replace("\u01A1\u0323", "\u1EE3")
		str = str.replace("\u01A1\u0303", "\u1EE1")
		str = str.replace("\u00F4\u0309", "\u1ED5")
		str = str.replace("\u00F4\u0301", "\u1ED1")
		str = str.replace("\u00F4\u0300", "\u1ED3")
		str = str.replace("\u00F4\u0323", "\u1ED9")
		str = str.replace("\u00F4\u0303", "\u1ED7")
		str = str.replace("\u0061\u0309", "\u1EA3")
		str = str.replace("\u0061\u0301", "\u00E1")
		str = str.replace("\u0061\u0300", "\u00E0")
		str = str.replace("\u0061\u0323", "\u1EA1")
		str = str.replace("\u0061\u0303", "\u00E3")
		str = str.replace("\u0103\u0309", "\u1EB3")
		str = str.replace("\u0103\u0301", "\u1EAF")
		str = str.replace("\u0103\u0300", "\u1EB1")
		str = str.replace("\u0103\u0323", "\u1EB7")
		str = str.replace("\u0103\u0303", "\u1EB5")
		str = str.replace("\u00E2\u0309", "\u1EA9")
		str = str.replace("\u00E2\u0301", "\u1EA5")
		str = str.replace("\u00E2\u0300", "\u1EA7")
		str = str.replace("\u00E2\u0323", "\u1EAD")
		str = str.replace("\u00E2\u0303", "\u1EAB")
		str = str.replace("\u0045\u0309", "\u1EBA")
		str = str.replace("\u0045\u0301", "\u00C9")
		str = str.replace("\u0045\u0300", "\u00C8")
		str = str.replace("\u0045\u0323", "\u1EB8")
		str = str.replace("\u0045\u0303", "\u1EBC")
		str = str.replace("\u00CA\u0309", "\u1EC2")
		str = str.replace("\u00CA\u0301", "\u1EBE")
		str = str.replace("\u00CA\u0300", "\u1EC0")
		str = str.replace("\u00CA\u0323", "\u1EC6")
		str = str.replace("\u00CA\u0303", "\u1EC4")
		str = str.replace("\u0059\u0309", "\u1EF6")
		str = str.replace("\u0059\u0301", "\u00DD")
		str = str.replace("\u0059\u0300", "\u1EF2")
		str = str.replace("\u0059\u0323", "\u1EF4")
		str = str.replace("\u0059\u0303", "\u1EF8")
		str = str.replace("\u0055\u0309", "\u1EE6")
		str = str.replace("\u0055\u0301", "\u00DA")
		str = str.replace("\u0055\u0300", "\u00D9")
		str = str.replace("\u0055\u0323", "\u1EE4")
		str = str.replace("\u0055\u0303", "\u0168")
		str = str.replace("\u01AF\u0309", "\u1EEC")
		str = str.replace("\u01AF\u0301", "\u1EE8")
		str = str.replace("\u01AF\u0300", "\u1EEA")
		str = str.replace("\u01AF\u0323", "\u1EF0")
		str = str.replace("\u01AF\u0303", "\u1EEE")
		str = str.replace("\u0049\u0309", "\u1EC8")
		str = str.replace("\u0049\u0301", "\u00CD")
		str = str.replace("\u0049\u0300", "\u00CC")
		str = str.replace("\u0049\u0323", "\u1ECA")
		str = str.replace("\u0049\u0303", "\u0128")
		str = str.replace("\u004F\u0309", "\u1ECE")
		str = str.replace("\u004F\u0301", "\u00D3")
		str = str.replace("\u004F\u0300", "\u00D2")
		str = str.replace("\u004F\u0323", "\u1ECC")
		str = str.replace("\u004F\u0303", "\u00D5")
		str = str.replace("\u01A0\u0309", "\u1EDE")
		str = str.replace("\u01A0\u0301", "\u1EDA")
		str = str.replace("\u01A0\u0300", "\u1EDC")
		str = str.replace("\u01A0\u0323", "\u1EE2")
		str = str.replace("\u01A0\u0303", "\u1EE0")
		str = str.replace("\u00D4\u0309", "\u1ED4")
		str = str.replace("\u00D4\u0301", "\u1ED0")
		str = str.replace("\u00D4\u0300", "\u1ED2")
		str = str.replace("\u00D4\u0323", "\u1ED8")
		str = str.replace("\u00D4\u0303", "\u1ED6")
		str = str.replace("\u0041\u0309", "\u1EA2")
		str = str.replace("\u0041\u0301", "\u00C1")
		str = str.replace("\u0041\u0300", "\u00C0")
		str = str.replace("\u0041\u0323", "\u1EA0")
		str = str.replace("\u0041\u0303", "\u00C3")
		str = str.replace("\u0102\u0309", "\u1EB2")
		str = str.replace("\u0102\u0301", "\u1EAE")
		str = str.replace("\u0102\u0300", "\u1EB0")
		str = str.replace("\u0102\u0323", "\u1EB6")
		str = str.replace("\u0102\u0303", "\u1EB4")
		str = str.replace("\u00C2\u0309", "\u1EA8")
		str = str.replace("\u00C2\u0301", "\u1EA4")
		str = str.replace("\u00C2\u0300", "\u1EA6")
		str = str.replace("\u00C2\u0323", "\u1EAC")
		str = str.replace("\u00C2\u0303", "\u1EAA")
		return str

	def replacePunct(self,str):
		str = str.replace("("," ")
		str = str.replace(")"," ")
		str = str.replace("!"," ")
		str = str.replace(".","")
		str = str.replace(","," ")
		str = str.replace(":"," ")
		str = str.replace("?"," ")
		# str = str.replace("n't","")
		str = str.replace("'s","")
		str = str.replace("'re","")
		str = str.replace("'d","")
		str = str.replace("'ll","")
		str = str.replace("--"," ")
		str = str.replace("'ve","")
		str = str.replace(";","")
		str = re.sub(r'(?is)\d+', ' ', str).strip()
		str = re.sub(r'(?is)\W+', ' ', str).strip()
		# str = str.replace("n't"," not")
		return str

	def removeStopword_stem(self,str):
		ps = PorterStemmer()
		stopWords = set(stopwords.words('english'))
		words_result = []
		words = word_tokenize(str)
		for word in words:
			if word not in stopWords:
				word = ps.stem(word)
				words_result.append(word)
		return words_result

	def Concate_list(self,list_str):
		sentence = ""
		for w in list_str:
			sentence = sentence + w + " "
		return sentence

	def Process_Str(self,str_):
		# str_result = self.replaceUnicode(str)
		str_result = self.replacePunct(str_)
		word_list = self.removeStopword_stem(str_result)
		result = self.Concate_list(word_list).replace("n't","not")
		return result
	def Process_data(self,datas):
		for data in datas:
			if data['review_title'] != None:
				data['review_title'] = self.Process_Str(data['review_title'])
			if data['review_body'] != None:
				data['review_body'] = self.Process_Str(data['review_body'])
		return datas

	def Process_File(self,file_name):
		datas = self.readFile(file_name)
		data_result = self.Process_data(datas)
		return data_result
	def write_File(self,input_filename,output_filename):

		print("chuẩn bị ghi")
		#key = ('rating','review_title','review_body',)
		datas = self.Process_File(input_filename)
		count = 1
		self.f = open(output_filename, "w", encoding='utf-8')
		self.f.write('[')
		for data in datas:
			if count == len(datas):
				#dic = dict.fromkeys(key, data)
				line = json.dumps(data, ensure_ascii=False) + "\n"
			else:
				count = count + 1
				#dic = dict.fromkeys(key, data)
				line = json.dumps(data, ensure_ascii=False) + ",\n"
			self.f.write(line)
		self.f.write(']')
		self.f.close()
		return output_filename

	def GetFiles(self, path):

		file_list = []
		for dir, subdirs, files in os.walk(path):
			file_list.extend([FJoin(dir, f) for f in files])
		return file_list

	def Process_path(self,path):
		list_file_Input = self.GetFiles(path)
		for file in list_file_Input:
			file_Out = file.replace('.json','(P).json')
			self.write_File(file,file_Out)


if __name__ =="__main__":

	i = Process_file()
	i.Process_path('/home/trang/Process_Pr/data_raw')





















