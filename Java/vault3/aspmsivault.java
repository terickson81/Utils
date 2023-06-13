import com.azure.identity.DefaultAzureCredentialBuilder;
import com.azure.core.credential.TokenCredential;
import com.azure.core.credential.AccessToken;
import com.bettercloud.vault.Vault;
import com.bettercloud.vault.VaultConfig;

public class AzureVaultAuthExample {
    public static void main(String[] args) throws Exception {
        TokenCredential defaultCredential = new DefaultAzureCredentialBuilder().build();
        AccessToken accessToken = defaultCredential.getToken("https://management.azure.com/.default").block();

        final VaultConfig config = new VaultConfig()
                .address("https://<your-vault-address>")
                .token(accessToken.getToken())
                .build();
        final Vault vault = new Vault(config);

        // After this, you can use `vault` to read and write secrets as needed:
        // String secret = vault.logical().read("secret/hello").getData().get("world");
    }
}
