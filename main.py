
#! /usr/bin/env python3
import os
import requests

def send_feedback():
        #dir = "C:/Users/Administrator/PycharmProjects/PostFeedbackREST_API/txt/"
        dir = "/data/feedback"
        feedback = {}
        for file in os.listdir(dir):
                feedback_file = open(dir + file, "r")
                list_feedback = feedback_file.readlines()
                feedback["title"] = list_feedback[0].rstrip('\n')
                feedback["name"] = list_feedback[1].rstrip('\n')
                feedback["date"] = list_feedback[2].rstrip('\n')
                feedback["feedback"] = list_feedback[3].rstrip('\n')
                print(feedback)
                response = requests.post("http://35.202.87.87/feedback/", json=feedback)
                print(response.request.body)
                response.raise_for_status()
                feedback_file.close()

if __name__ == '__main__':
        send_feedback()
