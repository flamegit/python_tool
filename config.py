#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import configparser
import argparse
import collections



# config = configparser.ConfigParser()
# print("- Empty config %s"%config.sections())

# print("- Load config file")
# config.read("./example.ini")
# ## 此处返回的sections list不包括 default
# print("> config sections : %s"%config.sections()) 
# print('bitbucket.org' in config )  ## 判断配置文件中是否存在该 section
# print("> Load config file is :")

# for section in config.keys():
#     print("[{s}]".format(s=section))
#     for key in config[section]:
#         print("{k} = {v}".format(k=key, v=config[section][key]))

# ## 如访问 dict 一样读取配置内容
# print("\n- Get value like dict :user =  %s"%config['bitbucket.org']['user'])
# conf_bitbucket = config['bitbucket.org']
# print(conf_bitbucket['user'])

# """
# The DEFAULT section which provides default values for all other sections"""
# print("\n- DEFAULT Section")
# ## default 是所有section的默认设置，备胎...
# for key in config['bitbucket.org']: print(key)
# print("> Get default value : forwardx11 = %s\n"%config['bitbucket.org']['forwardx11'])

# ## 读取不同数据类型的配置参数
# print("\n- Support datatypes")
# forwardx11 = config['bitbucket.org'].getboolean('forwardx11')
# int_port = config.getint('topsecret.server.com', 'port')
# float_port = config.getfloat('topsecret.server.com', 'port')
# print("> Get int port = %d type : %s"%(int_port, type(int_port)))
# print("> Get float port = %f type : %s"%(float_port, type(float_port)))

def readConifg(section ='student'):

	ConfigInfo = collections.namedtuple('ConfigInfo','src_path dest_path tinykey')
	config = configparser.ConfigParser()
	config.read('./config.ini')
	return ConfigInfo(config[section]['src_path'],config[section]['dest_path'],config[section]['tinykey'])

	

def main():
	parser = argparse.ArgumentParser(description = 'argparse test')
	parser.add_argument("-c", "--compress", help="compress or not",action="store_true")
	parser.add_argument("-f", "--file", metavar= "DD",help="file name",default= "adb")

	args = parser.parse_args()
	if(args.compress):
		print("need commpress")

	print(args.file)
	print(readConifg().tinykey)


if __name__ == "__main__":
    main()
