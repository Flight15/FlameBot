access_token=$(curl --location --request POST 'https://api.getport.io/v1/auth/access_token' --header 'Content-Type: application/json' --data-raw '{
    "clientId": "2gA7Yt4tsfH9RwRnbmp3ElzArMjNPmJr",
    "clientSecret": "TJO25UQCp1k4UJBZP6pHw5zGQ1ncJ4809A9GdPy2CE4Ne4ec3Ygj4BglmwBYnmJU"
    }' | jq -r '.accessToken')
    echo "PRINTING ACCESS TOKEN"
    echo $access_token

    repos=$(curl -X 'POST' \
    'https://api.getport.io/v1/entities/search?exclude_calculated_properties=false&attach_title_to_relation=false' \
    -H 'accept: */*' \
    -H "Authorization: Bearer $access_token" \
    -H 'Content-Type: application/json' \
    -d '{"combinator": "and",
        "rules":[
        {
            "property": "$blueprint",
            "operator": "=",
            "value": "repository"
        }
        ]
        }' | jq -r '.entities[].identifier')
        echo $repos
    echo "INITIALIZING FOR LOOP"
    for repo in $repos ; do
    res=$(curl -X 'POST' \
        'https://api.getport.io/v1/entities/search?exclude_calculated_properties=false&attach_title_to_relation=false' \
        -H 'accept: */*' \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $access_token" \
        -d "{
        \"combinator\": \"and\",
        \"rules\":[
        {
            \"blueprint\": \"repository\",
            \"operator\": \"relatedTo\",
            \"value\": \"$repo\"
        },
        {
            \"property\": \"severity\",
            \"operator\": \"=\",
            \"value\": \"low\"
        }
        ]
        }"
        )
        echo "done searching"
        echo $repo
        echo "CALCULATING COUNT"
        count=$(echo $res | jq '.entities | length')
        echo "PRINTING COUNT"
        echo $count
        patchbody='{"identifier": "$repo","properties": {"low_count": "$count" }}'
        curl -X 'PATCH' \
        "https://api.getport.io/v1/blueprints/repository/entities/$repo?create_missing_related_entities=false" \
        -H 'accept: */*' \
        -H "Authorization: Bearer $access_token" \
        -H 'Content-Type: application/json' \
        -d "{
        \"properties\": {
            \"low_count\": $count
        }
        }"
        echo "STARTING NEXT REPO"
    done
    echo "DONE"
