import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.vault.authentication.ClientAuthentication;
import org.springframework.vault.authentication.TokenAuthentication;
import org.springframework.vault.client.VaultEndpoint;
import org.springframework.vault.core.VaultTemplate;
import org.springframework.vault.support.VaultResponse;
import org.springframework.context.annotation.Bean;

import javax.annotation.PostConstruct;

@SpringBootApplication
public class VaultDemoApplication {

    @Value("${spring.cloud.vault.host}")
    String vaultHost;

    @Value("${spring.cloud.vault.port}")
    int vaultPort;

    @Value("${spring.cloud.vault.token}")
    String vaultToken;

    private static final String SECRET_MOUNT_POINT = "my-mount-point";

    public static void main(String[] args) {
        SpringApplication.run(VaultDemoApplication.class, args);
    }

    @Bean
    public VaultTemplate vaultTemplate() {
        VaultEndpoint vaultEndpoint = new VaultEndpoint();
        vaultEndpoint.setHost(vaultHost);
        vaultEndpoint.setPort(vaultPort);
        ClientAuthentication clientAuthentication = new TokenAuthentication(vaultToken);
        return new VaultTemplate(vaultEndpoint, clientAuthentication);
    }

    @PostConstruct
    public void getSecrets() {
        VaultTemplate vaultTemplate = vaultTemplate();
        String[] secrets = {"test1", "test2", "test3"};
        for (String secret : secrets) {
            String path = SECRET_MOUNT_POINT + "/data/" + secret; // Note the /data/ path segment when using KV V2
            VaultResponse response = vaultTemplate.read(path);
            if (response != null) {
                System.out.println("Secret " + secret + ": " + response.getData().get("data"));
            }
        }
    }
}
