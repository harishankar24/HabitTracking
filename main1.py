from confidential_data import pixela_token, username
import requests

pixela_endpoint = "https://pixe.la/v1/users"
pixela_endpoint_parameter = {
    "token": pixela_token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url = pixela_endpoint, json = pixela_endpoint_parameter)
# print(response.text)

#----------- Creating Graph ------------
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_endpoint_parameter = {
    "id":"graph1",
    "name":"Number of Pushups",
    "unit":"times",
    "type":"int",
    "color":"momiji"
}
headers = {
    "X-USER-TOKEN":pixela_token
}
# response = requests.post(url = graph_endpoint, json = graph_endpoint_parameter, headers = headers)
# print(response.text)

#---------- POSTING A PIXEL ---------------------------
post_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_endpoint_parameter['id']}"
post_pixel_endpoint_parameter = {
    "date":"20210127",
    "quantity":"45"
}
response = requests.post(url = post_pixel_endpoint, json = post_pixel_endpoint_parameter, headers = headers)
print(response.text)
