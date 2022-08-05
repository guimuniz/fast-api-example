from fastapi import Request


async def security_middleware(request: Request, call_next):
    response = await call_next(request)
    default_src = ' '.join(["self", "fastapi.tiangolo.com", "cdn.jsdelivr.net", "webpack", "http://www.w3.org"])
    scripts_src = ' '.join(["cdn.jsdelivr.net", "self", "'unsafe-inline'"])
    headers = {
        "Pragma": "no-cache",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "X-Content-Type-Options": "nosniff",
        "X-DNS-Prefetch-Control": "off",
        "X-Frame-Options": "deny",
        "X-XSS-Protection": "1; mode=block",
        "Strict-Transport-Security": "max-age=31536000 ; includeSubDomains",
        "X-Permitted-Cross-Domain-Policies": "none",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Content-Security-Policy": f"default-src 'self' {default_src}; script-src {scripts_src};",
    }
    for key, value in headers.items():
        response.headers[key] = value
    return response
