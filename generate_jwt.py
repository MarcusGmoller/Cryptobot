import jwt
from cryptography.hazmat.primitives import serialization
import time
import secrets

key_name       = "organizations/4d3e2a62-5c3e-4226-9cbb-386e489a2cfc/apiKeys/f4aa0aba-8612-4b1d-879c-62c188927561"
key_secret     = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIFezhedI+gsv+i8llJ7n52HtDE/2V1sltPCTiU5+kT+poAoGCCqGSM49\nAwEHoUQDQgAEMG5ruPlaW63jOv87nQnUflzJ13P4z1I6QffeLM4sBxRp1q8N3cNa\ndWkfFzUm2OHorjPJSvWeePiYxo7ePBV9CA==\n-----END EC PRIVATE KEY-----\n"
request_method = "GET"
request_host   = "api.coinbase.com"
request_path   = "/v2/accounts"

def build_jwt(uri):
    private_key_bytes = key_secret.encode('utf-8')
    private_key = serialization.load_pem_private_key(private_key_bytes, password=None)

    jwt_payload = {
        'sub': key_name,
        'iss': "coinbase-cloud",
        'nbf': int(time.time()),
        'exp': int(time.time()) + 120,
    }

    jwt_token = jwt.encode(
        jwt_payload,
        private_key,
        algorithm='ES256',
        headers={'kid': key_name, 'nonce': secrets.token_hex()},
    )

    return jwt_token

def main():
    uri = f"{request_method} {request_host}{request_path}"
    jwt_token = build_jwt(uri)
    print(f'export JWT="{jwt_token}"')

if __name__ == "__main__":
    main()

#kør echo $env:JWT i terminal