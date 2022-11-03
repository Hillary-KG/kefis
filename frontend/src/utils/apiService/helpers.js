export const getOidcStorageKey = () => {
  const authSettings = JSON.parse(localStorage.getItem("authSettings"));
  if (authSettings) {
    return `oidc.user:${authSettings.auth_server}:${authSettings.client_id}`;
  } else {
    const authSettings = {
      auth_server: "kefis-store",
      client_id: "frontend",
    };
    localStorage.setItem("authSettings", JSON.stringify(authSettings));
    const oidcKey = `oidc.user:${authSettings.auth_server}:${authSettings.client_id}`;
    localStorage.setItem(oidcKey, "{}");
    return oidcKey;
  }
};

export const getOidcInfo = () => {
  const key = getOidcStorageKey();
  if (key) {
    const oidc = JSON.parse(localStorage.getItem(key));
    return oidc;
  }
  return null;
};

export const getToken = () => {
  const oidc = getOidcInfo();
  if (oidc) {
    return oidc.id_token;
  }
  return null;
};

export const setToken = (token) => {
  const oidc = getOidcInfo();
  if (oidc) {
    oidc.id_token = token;
    localStorage.setItem(getOidcStorageKey(), JSON.stringify(oidc));
  }
};

export const deleteToken = () => {
  const oidc = getOidcInfo();
  if (oidc) {
    oidc.id_token = null;
    localStorage.setItem(getOidcStorageKey(), JSON.stringify(oidc));
  }
};