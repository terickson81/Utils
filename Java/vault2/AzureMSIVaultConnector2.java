import com.bettercloud.vault.*;
import com.bettercloud.vault.api.Auth;
import com.bettercloud.vault.response.AuthResponse;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.ResponseBody;
import org.json.JSONObject;

import java.io.IOException;

public class AzureMSIVaultConnector {
    private static final String VAULT_ADDR = "http://127.0.0.1:8200";
    private static final String VAULT_ROLE = "your-vault-role";
    private static final String AZURE_TOKEN_URL = "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F";

    public void retrieveSecrets() {
        try {
            OkHttpClient client = new OkHttpClient();
            Request request = new Request.Builder()
                    .url(AZURE_TOKEN_URL)
                    .addHeader("Metadata", "true")
                    .build();
            Response response = client.newCall(request).execute();
            if (response.isSuccessful()) {
                ResponseBody body = response.body();
                if (body != null) {
                    JSONObject json = new JSONObject(body.string());
                    String accessToken = json.getString("access_token");

                    final VaultConfig config = new VaultConfig().address(VAULT_ADDR).build();
                    final Vault vault = new Vault(config);

                    AuthResponse authResponse = vault.auth().loginByJwt("azure", VAULT_ROLE, accessToken);
                    String vaultToken = authResponse.getAuthClientToken();

                    // Set the Vault token on the config
                    config.token(vaultToken);

                    // Now use the Vault client as before
                    final String pathToSecret = "secret/hello";
                    final LogicalResponse logicalResponse = vault.logical().read(pathToSecret);
                    final String secretValue = logicalResponse.getData().get("value");

                    System.out.println("The secret value at 'secret/hello' is: " + secretValue);
                } else {
                    System.out.println("Error retrieving Azure access token");
                }
            } else {
                System.out.println("Error retrieving Azure access token");
            }
        } catch (VaultException | IOException e) {
            System.out.println("Error retrieving secret: " + e.getMessage());
        }
    }
}
