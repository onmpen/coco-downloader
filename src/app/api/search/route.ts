import { NextRequest, NextResponse } from 'next/server';
import { getProvider } from '@/lib/providers';

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const q = searchParams.get('q');
  const providerName = searchParams.get('provider');
  const limit = Math.min(Math.max(Number(searchParams.get('limit')) || 20, 1), 50);
  const offset = Math.max(Number(searchParams.get('offset')) || 0, 0);

  if (!q) {
    return NextResponse.json({ error: 'Missing query' }, { status: 400 });
  }

  const resolvedProviderName =
    providerName && providerName !== 'all' ? providerName : 'netease';
  const provider = getProvider(resolvedProviderName);
  const items = await provider.search(q, limit, offset);

  return NextResponse.json({ items });
}
