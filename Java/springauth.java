import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.web.authentication.AbstractAuthenticationProcessingFilter;
import org.springframework.security.web.util.matcher.RequestMatcher;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class CustomAuthenticationFilter extends AbstractAuthenticationProcessingFilter {

    public CustomAuthenticationFilter(RequestMatcher requiresAuthenticationRequestMatcher) {
        super(requiresAuthenticationRequestMatcher);
    }

    @Override
    public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response)
            throws AuthenticationException, IOException, ServletException {
        // The attemptAuthentication method is not invoked from doFilter in this example
        throw new UnsupportedOperationException("The attemptAuthentication method should not be called directly.");
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response,
                                    FilterChain filterChain) throws ServletException, IOException {
        // Invoke attemptAuthentication from within doFilterInternal
        try {
            Authentication authentication = attemptAuthentication(request, response);

            // If authentication is successful, set the security context
            if (authentication != null) {
                successfulAuthentication(request, response, filterChain, authentication);
            }
        } catch (AuthenticationException ex) {
            unsuccessfulAuthentication(request, response, ex);
        }
    }

    @Override
    protected void successfulAuthentication(HttpServletRequest request, HttpServletResponse response,
                                            FilterChain chain, Authentication authResult)
            throws IOException, ServletException {
        // Optionally, you can perform additional actions upon successful authentication
        // For example, you can generate and set a JWT token in the response header
        // or redirect the user to a specific page
        // ...

        // Continue the filter chain
        chain.doFilter(request, response);
    }

    protected void unsuccessfulAuthentication(HttpServletRequest request, HttpServletResponse response,
                                              AuthenticationException failed) throws IOException, ServletException {
        // Optionally, you can handle unsuccessful authentication attempts
        // For example, you can redirect the user to an error page or return an error response
        // ...

        // Continue the filter chain
        chain.doFilter(request, response);
    }
}
