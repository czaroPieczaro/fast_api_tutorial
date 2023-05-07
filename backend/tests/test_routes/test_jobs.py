import json

test_data = {
    "title": 1,
    "company": "test_company",
    "company_url": "test_company_url",
    "location": "test_location",
    "description": "test_description",
    "date_posted": "2022-03-20",
}


def test_create_job(client):
    response = client.post("/jobs/create-job/", content=json.dumps(test_data))
    assert response.status_code == 200
    assert response.json()["company"] == "test_company"
    assert response.json()["description"] == "test_description"


def test_read_job(client):
    data = test_data
    client.post("/jobs/create-job/", content=json.dumps(data))

    response = client.get("/jobs/1")
    assert response.status_code == 200
    assert response.json()["company"] == "test_company"
    assert response.json()["description"] == "test_description"


def test_failed_read_job(client):
    response = client.get("/jobs/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Job with id 1 does not exist."


def test_list_jobs(client):
    client.post("/jobs/create-job/", content=json.dumps(test_data))
    client.post("/jobs/create-job/", content=json.dumps(test_data))

    response = client.get("/jobs/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    client.post("/jobs/create-job/", content=json.dumps(test_data))
    updated_data = test_data.copy()
    updated_data["title"] = "test new title"
    response = client.put("jobs/update/1", content=json.dumps(updated_data))
    assert response.json()["msg"] == "Successfully updated data."
