@Configuration
public class App1ServletConfig {

    @Bean
    public ServletRegistrationBean<DispatcherServlet> app1DispatcherServletRegistration() {
        DispatcherServlet dispatcherServlet = new DispatcherServlet();
        ServletRegistrationBean<DispatcherServlet> registrationBean = new ServletRegistrationBean<>(dispatcherServlet, "/app1/*");
        registrationBean.setLoadOnStartup(1);
        return registrationBean;
    }
}
