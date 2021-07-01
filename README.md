# Image-upload

`How to run Project`

cmd: python3 manage.py runserver

`API Description`:

| Method        | API                                  | Function    |
| ------------- | -------------------------------------| ----------- |
| POST          | imageupload/add-member               | Add user    |
| POST          | imageupload/my/images/<str:m_id>     | Add image   |
| GET           | imageupload/my/images/<str:m_id>     | Get Image   |


`Usage`:

1. Add a user using Add user API.

2. Use user token genretated from add user's API to upload new Image.

3. Get all images(of one user) usig same token.
