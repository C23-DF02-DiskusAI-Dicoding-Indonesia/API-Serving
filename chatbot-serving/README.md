# Chatbot Serving
```bash
docker pull antsaka/chatbot-serving:integrated
```
This code implements a serving API for a chatbot. Let's break it down:

* The code imports necessary modules such as Flask, render_template, request, jsonify, flask_cors, tensorflow, tensorflow_hub, and json.

* An instance of the Flask application is created with Flask(__name__), and CORS (Cross-Origin Resource Sharing) is enabled for the Flask application using CORS(app).

* The code loads the results from a JSON file named 'results.json' using json.load(f). These results likely contain information about modules, discussion titles, and discussion links.

* The Universal Sentence Encoder (USE) module is loaded from the URL "https://tfhub.dev/google/universal-sentence-encoder/4" using hub.load(module_url).

* The root route '/' is defined, and when accessed, it returns the string "API is running."

* The /predict route is defined with the methods=['POST'] parameter to handle POST requests. This route expects a JSON payload with a key "question" containing the user's question.

* Inside the /predict route, the input question is embedded using the Universal Sentence Encoder by calling embed([question]).

* The code calculates cosine similarity scores between the embedded question and the pre-embedded modules stored in the results variable.

* The scores are sorted in descending order, and the top 3 modules, their titles, and links are extracted.

* The module names, titles, and links are combined into an HTML paragraph format with separators.

* The response is formatted as a JSON object containing the combined paragraph.

* The Flask application is run with app.run(host='0.0.0.0', port=2000) to start the API on the specified host and port.

Overall, this code sets up an API that accepts a question, calculates the similarity between the question and pre-defined modules using the Universal Sentence Encoder, and returns the top module titles and links as a combined HTML paragraph in the API response.

Note: The parameters used in this code are the default parameters for Flask and TensorFlow. You can modify them as per your requirements, such as changing the host and port for the API.


## Screenshots

The resulting parameter in the JSON response is as follows:

<p align="center">
    <img width="908" alt="Screenshot 2023-06-08 at 22 38 45" src="https://github.com/C23-DF02-DiskusAI-Dicoding-Indonesia/API-Serving/assets/132810595/9467490c-49ff-4eb7-b38d-2f9c2e8cb510">
</p>
* combined_paragraph: This parameter contains an HTML paragraph that combines information from the top relevant modules based on the given question. The paragraph includes module names, titles, and discussion links. These modules are the most similar ones to the question based on the calculated cosine similarity using the Universal Sentence Encoder. The paragraph can be used to display the chatbot's prediction results to the user.
Each paragraph within combined_paragraph consists of three HTML elements: Module, Title, and Link. The module and title information are enclosed in "p" tags, while the discussion link is displayed within an "a" tag.


The resulting parameter in the DiskusAI is as follows:
<p align="center">
    <img width="588" alt="Screenshot 2023-06-08 at 22 39 23" src="https://github.com/C23-DF02-DiskusAI-Dicoding-Indonesia/API-Serving/assets/132810595/9e54dc9f-ba17-42cb-8a7b-7b3cc19abfe5">
</p>
