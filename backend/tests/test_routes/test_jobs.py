import json

from fastapi import status

test_data = {
    "title": 1,
    "company": "test_company",
    "company_url": "test_company_url",
    "location": "test_location",
    "description": "test_description",
    "date_posted": "2022-03-20",
}


def test_create_job(client, normal_user_token_headers):
    response = client.post(
        "/jobs/create-job/",
        content=json.dumps(test_data),
        headers=normal_user_token_headers,
    )
    assert response.status_code == 200
    assert response.json()["company"] == "test_company"
    assert response.json()["description"] == "test_description"


def test_read_job(client, normal_user_token_headers):
    data = test_data
    client.post(
        "/jobs/create-job/", content=json.dumps(data), headers=normal_user_token_headers
    )

    response = client.get("/jobs/1")
    assert response.status_code == 200
    assert response.json()["company"] == "test_company"
    assert response.json()["description"] == "test_description"


def test_failed_read_job(client):
    response = client.get("/jobs/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Job with id 1 does not exist."


def test_list_jobs(client, normal_user_token_headers):
    client.post(
        "/jobs/create-job/",
        content=json.dumps(test_data),
        headers=normal_user_token_headers,
    )
    client.post(
        "/jobs/create-job/",
        content=json.dumps(test_data),
        headers=normal_user_token_headers,
    )

    response = client.get("/jobs/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client, normal_user_token_headers):
    client.post(
        "/jobs/create-job/",
        content=json.dumps(test_data),
        headers=normal_user_token_headers,
    )
    updated_data = test_data.copy()
    updated_data["title"] = "test new title"
    response = client.put(
        "jobs/update/1",
        content=json.dumps(updated_data),
        headers=normal_user_token_headers,
    )
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_a_job(client, normal_user_token_headers):
    client.post(
        "/jobs/create-job/",
        content=json.dumps(test_data),
        headers=normal_user_token_headers,
    )
    response_del = client.delete("jobs/delete/1", headers=normal_user_token_headers)
    response = client.get("/jobs/1")
    assert response_del.json()["msg"] == "Successfully deleted data."
    assert response.status_code == status.HTTP_404_NOT_FOUND
