# Searchbar Serving
```bash
docker pull antsaka/searchbar-serving:base
```
The model is a Flask-based API that provides suggestions based on a given query. It uses a pre-trained TensorFlow model and a tokenizer to generate the suggestions. Here's a summary of the model:

* The API is built using Flask and enables Cross-Origin Resource Sharing (CORS) to handle requests from different domains.
* The pre-trained model is loaded from a file called 'model.h5'. We have prepared 'five' H5 models that can be used for serving, but in this repository, the best one has been selected to generate its parameters. [Trained Data](https://drive.google.com/drive/folders/1C6hTM9CHSrO-dM_goDOuH17QWHy__a-J?usp=drive_link)
* The tokenizer is loaded from a JSON file called 'tokenizer.json'.
* The '/' endpoint simply returns the text "API is running." to indicate that the API is operational.
* The '/suggest' endpoint handles POST requests and expects a 'query' parameter in the form data.
* The 'query' parameter represents the user's input for which suggestions are requested.
* The tokenizer converts the 'query' into token sequences.
* The token sequences are padded to match the input shape of the loaded model.
* The model predicts the most likely suggestions for the given input.
* The top three predicted suggestions are selected and converted into human-readable format.
* The suggestions are returned as a JSON response.
Overall, the model serves as an API for generating suggestions based on user queries using a pre-trained TensorFlow model and a tokenizer. It provides a straightforward way to integrate suggestion functionality into applications.

## Screenshots
The expected parameter format for the API is:

![image](https://github.com/C23-DF02-DiskusAI-Dicoding-Indonesia/API-Serving/assets/76771393/92b348f8-3051-4d1f-8504-a9cb1666d533)

The returned result is a JSON object with the key 'suggestions' containing a list of suggestions. Each suggestion is a string that combines the 'query' with the found words in the model.

[Trained Data](https://drive.google.com/drive/folders/1C6hTM9CHSrO-dM_goDOuH17QWHy__a-J?usp=drive_link)
