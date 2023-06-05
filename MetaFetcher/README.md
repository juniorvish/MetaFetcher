# MetaFetcher

MetaFetcher is an API that takes a URL as input and returns the metadata in JSON format. The request and response have a consistent JSON body with the same parameter names.

## Installation

Clone the repository:

```
git clone https://github.com/juniorvish/MetaFetcher.git
```

Navigate to the project directory:

```
cd MetaFetcher
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the application:

```
python app.py
```

The API will be available at `http://localhost:5000`.

To fetch metadata, send a POST request to `http://localhost:5000/fetch` with the following JSON body:

```json
{
  "url": "https://example.com"
}
```

The response will be a JSON object containing the metadata:

```json
{
  "title": "Example Title",
  "description": "Example Description",
  "image": "https://example.com/image.jpg",
  "url": "https://example.com"
}
```