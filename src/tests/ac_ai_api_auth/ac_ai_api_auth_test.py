import pytest
from ac_ai_api_auth.models import AcAiApiUser as User


@pytest.fixture
def user(request, db):
    user = User.objects.create(username='test_user', email='test_email@test.com')
    user.set_password('test_password')
    user.save()
    return user


def test_login(client, user):
    assert client.get('/login/').status_code == 200
    resp = client.post('/login/', {'username': 'test_user', 'password': 'test_password'})
    assert resp.status_code == 302


def test_logout(client, user):
    client.force_login(user)
    resp = client.get('/logout/')
    assert resp.status_code == 302
