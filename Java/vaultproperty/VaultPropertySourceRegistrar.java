import org.springframework.context.annotation.Configuration;
import org.springframework.vault.core.VaultTemplate;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.env.EnvironmentPostProcessor;
import org.springframework.core.env.ConfigurableEnvironment;

@Configuration
public class VaultPropertySourceRegistrar implements EnvironmentPostProcessor {

    @Override
    public void postProcessEnvironment(ConfigurableEnvironment environment, SpringApplication application) {
        VaultTemplate vaultTemplate = ... // Create an instance of VaultTemplate with appropriate configuration

        VaultPropertySource propertySource = new VaultPropertySource(vaultTemplate);
        environment.getPropertySources().addFirst(propertySource);
    }
}
