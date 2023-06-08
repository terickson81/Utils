import com.bettercloud.vault.Vault;
import com.bettercloud.vault.VaultConfig;
import com.bettercloud.vault.VaultException;
import com.bettercloud.vault.response.LogicalResponse;

public class VaultConnector {
    private final String vaultAddr;
    private final String vaultToken;

    public VaultConnector(String vaultAddr, String vaultToken) {
        this.vaultAddr = vaultAddr;
        this.vaultToken = vaultToken;
    }

    public void retrieveSecrets() {
        try {
            final VaultConfig config = new VaultConfig()
                    .address(vaultAddr)
                    .token(vaultToken)
                    .build();

            final Vault vault = new Vault(config);
            final String pathToSecret = "secret/hello";

            final LogicalResponse response = vault.logical()
                    .read(pathToSecret);

            final String secretValue = response.getData().get("value");
            System.out.println("The secret value at 'secret/hello' is: " + secretValue);
        } catch (VaultException e) {
            System.out.println("Error retrieving secret: " + e.getMessage());
        }
    }
}
