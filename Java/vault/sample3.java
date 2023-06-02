import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.vault.core.VaultOperations;

@SpringBootApplication
public class VaultDemoApplication {

    @Autowired
    private VaultOperations vaultOperations;

    public static void main(String[] args) {
        SpringApplication.run(VaultDemoApplication.class, args);
    }

    @PostConstruct
    public void getSecrets() throws URISyntaxException {
        String[] secrets = {"test1", "test2", "test3"};
        for (String secret : secrets) {
            String path = "my-mount-point/data/" + secret; // Note the /data/ path segment when using KV V2
            VaultResponseSupport<Map> response = vaultOperations.read(path, Map.class);
            if (response != null) {
                System.out.println("Secret " + secret + ": " + response.getData().get("data"));
            }
        }
    }
}


--------------
  
 import org.springframework.context.annotation.Configuration;

@Configuration
public class VaultConfig {

    @Value("${spring.cloud.vault.host}")
    String vaultHost;

    @Value("${spring.cloud.vault.port}")
    int vaultPort;

    @Value("${spring.cloud.vault.token}")
    String vaultToken;

    @Bean
    public VaultOperations vaultOperations() throws URISyntaxException {
        VaultEndpoint vaultEndpoint = VaultEndpoint.from(new URI(vaultHost));
        ClientAuthentication clientAuthentication = new TokenAuthentication(vaultToken);
        HttpComponentsClientHttpRequestFactory requestFactory = ClientHttpRequestFactoryFactory.create(new ClientOptions(), SslConfiguration.unconfigured());
        VaultTemplate vaultTemplate = new VaultTemplate(vaultEndpoint, requestFactory, clientAuthentication);
        return vaultTemplate;
    }
}
