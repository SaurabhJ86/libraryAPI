import requests

# ENDPOINT = "http://127.0.0.1:8009/api/"

# def run_tests(method="get",data={}):

# 	r = requests.request(method,ENDPOINT,data=data)
# 	print(r.text)
# 	return r

ENDPOINT = "http://127.0.0.1:8009/api/"
def run_test(method="get",data={}):

	id_ = data.get("id",None)
	if id_ and method in ["put","delete","get"]:
		r = requests.request(method,ENDPOINT + str(id_) + "/",data=data)
	else:
		r = requests.request(method,ENDPOINT,data=data)
	print(r.text)
	return r

# To POST/Create data 
# run_test(method="post",data={"user":1,"name":"Another Great Theory","author":"Phil Thomas","pages":235,"ratings":4.2})

# To GET/Retrieve Single Data
# run_test(method="get",data={"id":4})

# To PUT/Update data
# run_test(method="put",data={"user":1,"id":2,"pages":500,"author":"Sanjeev Sanyal","name":"The Land of Seven Rivers","ratings":4.50})

# To DELETE/Destroy Single Data
# run_test(method="delete",data={"id":4})

# To LIST/LIST upon user ID
# run_test(method="get",data={"user":1})