import json


def test_create_job(client):
    data = {
        "title": "test_title",
        "company": "test_company",
        "company_url": "test_company_url",
        "location": "test_location",
        "description": "test_description",
        "date_posted": "2022-03-20",
    }
    response = client.post("/create-jobs/", content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "test_company"
    assert response.json()["description"] == "test_description"
