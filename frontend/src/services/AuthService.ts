import { instance } from "../api.config";

class AuthService {
  login(username: string, password: string) {
    return instance.post('/users/api/v1/token/', { username, password })
  }

  refreshToken(refresh: string) {
    return instance.post('/users/api/v1/token/refresh/', { refresh });
  }
}

export default new AuthService();
