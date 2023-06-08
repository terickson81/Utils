public class Main {
    public static void main(String[] args) {
        VaultConnector vaultConnector = new VaultConnector("http://127.0.0.1:8200", "your-token");
        vaultConnector.retrieveSecrets();
    }
}
